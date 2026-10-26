"""Potential flow over a semicircular hill (upper half of a circular cylinder).

Analytical solution, not a Navier–Stokes numerical simulation.
Dependencies: numpy, matplotlib, pillow (only for GIF), ffmpeg (only for MP4).
Run: python semicircular_hill_flow.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, PillowWriter
from matplotlib.colors import Normalize
from matplotlib.patches import Wedge

# --- Physical / visualization parameters ---
U = 1.0                     # uniform wind speed far upstream
A = 1.0                     # hill radius
XMIN, XMAX = -4.5*A, 6.0*A
YMIN, YMAX = 0.0, 3.5*A
DURATION = 12.0             # simulated time, in units A/U
FPS = 30
FRAMES = 360
NUM_PARTICLES = 280
OUTPUT = 'semicircular_hill_flow.mp4'
SEED = 7

# Cartesian velocities from Phi = U(r + a^2/r)cos(theta):
# ux = U[1 - a^2(x^2-y^2)/(x^2+y^2)^2]
# uy = -2 U a^2 xy/(x^2+y^2)^2
# Streamfunction: Psi = U*y*(1-a^2/(x^2+y^2)).
def velocity(x, y):
    r2 = np.maximum(x*x+y*y, 1e-12)
    ux = U*(1.0-A*A*(x*x-y*y)/(r2*r2))
    uy = -2.0*U*A*A*x*y/(r2*r2)
    return ux, uy

# Under the hill is solid; no fluid trajectories plotted there.
xg = np.linspace(XMIN, XMAX, 360)
yg = np.linspace(YMIN, YMAX, 160)
X, Y = np.meshgrid(xg, yg)
VX, VY = velocity(X, Y)
SOLID = (X*X + Y*Y <= A*A)
SPEED = np.ma.array(np.hypot(VX, VY)/U, mask=SOLID)
VX_M = np.ma.array(VX, mask=SOLID)
VY_M = np.ma.array(VY, mask=SOLID)

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(12.5, 5.5), facecolor='white')
fig.subplots_adjust(left=.065, right=.88, top=.87, bottom=.14)

# Constant Eulerian speed field (the solution is steady).
mesh = ax.pcolormesh(X/A, Y/A, SPEED, cmap='turbo', norm=Normalize(0, 2), shading='auto', rasterized=True)
cb = fig.colorbar(mesh, ax=ax, pad=.018, fraction=.038)
cb.set_label(r'Speed $|\mathbf{u}|/U$')

# Actual instantaneous streamlines: Psi = constant. Only draw in fluid domain.
ax.streamplot(xg/A, yg/A, VX_M, VY_M, density=(1.25, .9), color='#23314a',
              linewidth=.55, arrowsize=.65, minlength=.3, maxlength=8,
              integration_direction='both', zorder=2)

hill = Wedge((0,0), 1, 0, 180, facecolor='#d8dbe1', edgecolor='#141b2b', linewidth=2.2, zorder=7)
ax.add_patch(hill)
ax.plot([XMIN/A, XMAX/A], [0,0], color='#141b2b', lw=2.4, zorder=8)

# Tracer particles entering from upstream. RK4 provides accurate trajectories.
rng = np.random.default_rng(SEED)
px = rng.uniform(XMIN, XMAX, NUM_PARTICLES)  # initialize throughout domain
py = rng.uniform(.12*A, YMAX*.95, NUM_PARTICLES)
# Remove any initially inside solid (reset at inlet).
inside = px*px+py*py <= (A*1.015)**2
px[inside] = XMIN
py[inside] = rng.uniform(.12*A, YMAX*.95, inside.sum())
sc = ax.scatter(px/A, py/A, s=7.5, c='white', edgecolors='#14213d', linewidths=.24,
                alpha=.93, zorder=5)

# A closed material contour: its deformation illustrates the actual flow.
# Initialize a circular patch of fluid above the hill.
phi = np.linspace(0, 2*np.pi, 100)
patch_x = -2.5*A + .18*A*np.cos(phi)
patch_y = 1.0*A + .18*A*np.sin(phi)
outline, = ax.plot(patch_x/A, patch_y/A, color='#f8fafc', lw=2.8, zorder=6)
outline_inner, = ax.plot(patch_x/A, patch_y/A, color='#172033', lw=.8, zorder=6)

ax.set(xlim=(XMIN/A, XMAX/A), ylim=(YMIN/A,YMAX/A),
       xlabel=r'$x/a$', ylabel=r'$y/a$')
ax.set_aspect('equal', adjustable='box')
ax.set_title('Potential flow over a semicircular hill', fontsize=17, weight='bold', pad=14)
time_label = ax.text(.017, .965, '', transform=ax.transAxes, va='top', ha='left',
                     fontsize=11, color='white', bbox=dict(facecolor='#172033', alpha=.9, edgecolor='none', pad=6), zorder=10)
ax.text(.98,.965, r'$\Phi=U(r+a^2/r)\cos\theta$', transform=ax.transAxes,
        ha='right', va='top', fontsize=12, color='white',
        bbox=dict(facecolor='#172033', alpha=.9, edgecolor='none', pad=6), zorder=10)

def step_rk4(x, y, dt):
    k1x,k1y = velocity(x,y)
    k2x,k2y = velocity(x+.5*dt*k1x, y+.5*dt*k1y)
    k3x,k3y = velocity(x+.5*dt*k2x, y+.5*dt*k2y)
    k4x,k4y = velocity(x+dt*k3x, y+dt*k3y)
    return (x + dt*(k1x+2*k2x+2*k3x+k4x)/6,
            y + dt*(k1y+2*k2y+2*k3y+k4y)/6)

# For repeatable playback, every frame is derived from initial conditions by
# precomputing the complete sequence (also makes seeking/saving stable).
dt = DURATION/(FRAMES-1)
particle_frames = np.empty((FRAMES, NUM_PARTICLES, 2), dtype=np.float32)
contour_frames = np.empty((FRAMES, len(phi), 2), dtype=np.float32)
for frame in range(FRAMES):
    particle_frames[frame,:,0] = px/A
    particle_frames[frame,:,1] = py/A
    contour_frames[frame,:,0] = patch_x/A
    contour_frames[frame,:,1] = patch_y/A
    if frame == FRAMES-1:
        break
    px, py = step_rk4(px, py, dt)
    patch_x, patch_y = step_rk4(patch_x, patch_y, dt)
    # Reinject tracers exiting downstream, maintaining continuous flow.
    escaped = (px>XMAX) | (py>YMAX) | (px<XMIN) | (py<0)
    px[escaped] = XMIN + rng.uniform(0, .08*A, escaped.sum())
    py[escaped] = rng.uniform(.12*A, .95*YMAX, escaped.sum())


def update(frame):
    sc.set_offsets(particle_frames[frame])
    outline.set_data(contour_frames[frame,:,0], contour_frames[frame,:,1])
    outline_inner.set_data(contour_frames[frame,:,0], contour_frames[frame,:,1])
    time_label.set_text(f't U/a = {frame*dt*U/A:.2f}')
    return sc, outline, outline_inner, time_label

ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=False, repeat=True)
if __name__ == '__main__':
    try:
        ani.save(OUTPUT, writer=FFMpegWriter(fps=FPS, bitrate=3500, codec='libx264',
                                               extra_args=['-pix_fmt', 'yuv420p']))
        print(f'Saved {OUTPUT}')
    except (FileNotFoundError, RuntimeError) as exc:
        print(f'MP4 export unavailable ({exc}). Saving GIF instead.')
        ani.save('semicircular_hill_flow.gif', writer=PillowWriter(fps=20))
    plt.close(fig)
