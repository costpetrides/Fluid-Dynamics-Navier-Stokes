import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter
from matplotlib.colors import Normalize
from matplotlib.patches import Wedge

U, A = 1.0, 1.0
XMIN, XMAX = -4.5*A, 6.0*A
YMIN, YMAX = 0.0, 3.5*A
DURATION, FPS, FRAMES = 12.0, 30, 360
NUM_PARTICLES, SEED = 280, 7
OUTPUT = 'semicircular_hill_three_elements.mp4'


def velocity(x, y):
    r2 = np.maximum(x*x + y*y, 1e-12)
    ux = U * (1 - A*A*(x*x-y*y)/(r2*r2))
    uy = -2*U*A*A*x*y/(r2*r2)
    return ux, uy


def step_rk4(x, y, dt):
    k1x, k1y = velocity(x, y)
    k2x, k2y = velocity(x + dt*k1x/2, y + dt*k1y/2)
    k3x, k3y = velocity(x + dt*k2x/2, y + dt*k2y/2)
    k4x, k4y = velocity(x + dt*k3x, y + dt*k3y)
    return (x + dt*(k1x+2*k2x+2*k3x+k4x)/6,
            y + dt*(k1y+2*k2y+2*k3y+k4y)/6)


xg = np.linspace(XMIN, XMAX, 360)
yg = np.linspace(YMIN, YMAX, 160)
X, Y = np.meshgrid(xg, yg)
VX, VY = velocity(X, Y)
solid = X*X + Y*Y <= A*A
speed = np.ma.array(np.hypot(VX, VY)/U, mask=solid)
VX = np.ma.array(VX, mask=solid)
VY = np.ma.array(VY, mask=solid)

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(12.5, 5.5), facecolor='white')
fig.subplots_adjust(left=.065, right=.88, top=.87, bottom=.14)

mesh = ax.pcolormesh(X/A, Y/A, speed, cmap='turbo', norm=Normalize(0, 2),
                     shading='auto', rasterized=True)
cb = fig.colorbar(mesh, ax=ax, pad=.018, fraction=.038)
cb.set_label(r'Speed $|\mathbf{u}|/U$')

ax.streamplot(xg/A, yg/A, VX, VY, density=(1.25, .9), color='#23314a',
              linewidth=.55, arrowsize=.65, minlength=.3, maxlength=8,
              integration_direction='both', zorder=2)

ax.add_patch(Wedge((0, 0), 1, 0, 180, facecolor='#d8dbe1',
                   edgecolor='#141b2b', linewidth=2.2, zorder=7))
ax.plot([XMIN/A, XMAX/A], [0, 0], color='#141b2b', lw=2.4, zorder=8)

rng = np.random.default_rng(SEED)
px = rng.uniform(XMIN, XMAX, NUM_PARTICLES)
py = rng.uniform(.12*A, .95*YMAX, NUM_PARTICLES)
inside = px*px + py*py <= (1.015*A)**2
px[inside] = XMIN
py[inside] = rng.uniform(.12*A, .95*YMAX, inside.sum())

sc = ax.scatter(px/A, py/A, s=7.5, c='white', edgecolors='#14213d',
                linewidths=.24, alpha=.93, zorder=5)

# Three closed material elements: near, middle, far
phi = np.linspace(0, 2*np.pi, 121)
initial_loops = [
    (-2.5*A, 0.42*A, 0.13*A),
    (-2.5*A, 1.00*A, 0.18*A),
    (-2.5*A, 2.65*A, 0.18*A),
]

loops = []
artists = []

for xc, yc, radius in initial_loops:
    lx = xc + radius*np.cos(phi)
    ly = yc + radius*np.sin(phi)
    loops.append([lx, ly])
    (line,) = ax.plot(lx/A, ly/A, color='white', lw=2.8,
                      zorder=6, solid_joinstyle='round')
    artists.append(line)

ax.set(xlim=(XMIN/A, XMAX/A), ylim=(YMIN/A, YMAX/A),
       xlabel=r'$x/a$', ylabel=r'$y/a$')
ax.set_aspect('equal', adjustable='box')
ax.set_title('Potential flow over a semicircular hill', fontsize=17,
             weight='bold', pad=14)

time_label = ax.text(.017, .965, '', transform=ax.transAxes,
                     va='top', ha='left', fontsize=11, color='white',
                     bbox=dict(facecolor='#172033', alpha=.9,
                               edgecolor='none', pad=6),
                     zorder=10)

ax.text(.98, .965, r'$\Phi=U(r+a^2/r)\cos\theta$', transform=ax.transAxes,
        ha='right', va='top', fontsize=12, color='white',
        bbox=dict(facecolor='#172033', alpha=.9,
                  edgecolor='none', pad=6), zorder=10)

dt = DURATION/(FRAMES-1)
particle_frames = np.empty((FRAMES, NUM_PARTICLES, 2), dtype=np.float32)
loop_frames = np.empty((FRAMES, len(initial_loops), len(phi), 2), dtype=np.float64)

for frame in range(FRAMES):
    particle_frames[frame, :, 0] = px/A
    particle_frames[frame, :, 1] = py/A

    for j, (lx, ly) in enumerate(loops):
        loop_frames[frame, j, :, 0] = lx/A
        loop_frames[frame, j, :, 1] = ly/A

    if frame == FRAMES - 1:
        break

    px, py = step_rk4(px, py, dt)

    for j, (lx, ly) in enumerate(loops):
        loops[j] = list(step_rk4(lx, ly, dt))
        # preserve exact closure
        loops[j][0][-1] = loops[j][0][0]
        loops[j][1][-1] = loops[j][1][0]

    escaped = (px > XMAX) | (py > YMAX) | (px < XMIN) | (py < 0)
    px[escaped] = XMIN + rng.uniform(0, .08*A, escaped.sum())
    py[escaped] = rng.uniform(.12*A, .95*YMAX, escaped.sum())


def update(frame):
    sc.set_offsets(particle_frames[frame])

    for j, artist in enumerate(artists):
        artist.set_data(loop_frames[frame, j, :, 0],
                        loop_frames[frame, j, :, 1])

    time_label.set_text(f't U/a = {frame*dt*U/A:.2f}')
    return (sc, *artists, time_label)


if __name__ == '__main__':
    ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS,
                        blit=False, repeat=True)
    try:
        ani.save(OUTPUT, writer=FFMpegWriter(
            fps=FPS,
            bitrate=3500,
            codec='libx264',
            extra_args=['-pix_fmt', 'yuv420p']
        ))
        print(f'Saved {OUTPUT}')
    except (FileNotFoundError, RuntimeError) as exc:
        print(f'MP4 unavailable ({exc}); saving GIF instead.')
        ani.save('semicircular_hill_three_elements.gif',
                 writer=PillowWriter(fps=20))
    plt.close(fig)
