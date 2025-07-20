# 1. 2D Shallow Water Simulation

## Introduction
Welcome to the 2D Shallow Water Simulation project [Simiulation](https://github.com/costpetrides/Fluid-Dynamics/blob/main/Simulations.ipynb)! This repository contains a numerical simulation designed to solve the 2D shallow water equations using finite differences. By modeling the momentum equations linearly and solving the continuity equation in its nonlinear form, this project provides insights into fluid dynamics in shallow water contexts under various conditions.

The simulation produced videos that visualize 
 - `Surface η(x,y,t) elevation`
 - `Velocity field`

The simulation also calculates parameters like:
 - `Rossby radius`
 - `Rossby number`
 - `Long Rossby wave speed`
 - `Long Rossb  transit time`


## Initial Parameters

  - `Length of domain in x-direction`
  - `Length of domain in y-direction`
  - `Acceleration of gravity [m/s^2]`
  - `Depth of fluid [m]`
  - `Fixed part ofcoriolis parameter f [1/s]`
  - `Gradient of coriolis parameter β [1/ms]`
  - `Density of fluid [kg/m^3)]`
  - `Amplitude of wind stress [kg/ms^2]`
  -   - `Friction [kg/ms^2]`

Is not mantantory to use all use parameters. Fell free to play with different initial conditions and senarios !!


## Theoretical Background
The simulation leverages a set of partial differential equations known as the shallow water equations, which describe fluid flow under a free surface in a fluid layer of constant density.

### Equations
- **Momentum Equations:**
  - In the x-direction: `du/dt - fv = -g * d(eta)/dx + tau_x / (rho_0 * H) - kappa * u`
  - In the y-direction: `dv/dt + fu = -g * d(eta)/dy + tau_y / (rho_0 * H) - kappa * v`
- **Continuity Equation:** `d(eta)/dt + d((eta + H) * u)/dx + d((eta + H) * v)/dy = sigma - w`

### Rossby Number and Linear Approximation
The Rossby number (Ro) is a dimensionless parameter that indicates the ratio of inertial to Coriolis forces in geophysical fluid dynamics. It is given by:

`Ro = U / (L * f)`

where:
- `U` is the characteristic velocity of the flow.
- `L` is the characteristic length scale of the motion.
- `f` is the Coriolis parameter.

A low Rossby number signifies that the Coriolis effect is dominant over inertial forces, which justifies the linear approximation of the momentum equations in large-scale geophysical flows.

## Some Trials !
The simulation was executed four times to explore the dynamics under different conditions. The simulation produced videos that visualize the surface elevation and velocity field! 

- use_coriolis = True
- use_beta = True
- use_friction = True
- use_wind = False
- use_source = False
- use_sink = False
- g = 9.81
- H = 100
- dx = 6711.41 km
- dy = 6711.41 km
- dt = 21.43 s
- kappa = 2.31481e-06
- kappa/beta = 115.741 km
- f_0 = 0.0001
- Max alpha = 0.00235707

- Rossby radius: 313.2 km
- Rossby number: 0.313209
- Long Rossby wave speed: 1.962 m/s
- Long Rossby transit time: 5.90 days




<p align="center">
  <a href="https://drive.google.com/file/d/1YR8FDIVf6ByGHbSNfJscaeu65GOWXCBM/view?usp=sharing" target="_blank">
    <img src="hta_1.gif" width="300" alt="Shallow Water  Simulation Results for H=10m">
  </a>
</p>




# 2. Kelvin-Helmholtz Instability Simulation

## Introduction
This repository contains also a Python script designed to simulate the Kelvin-Helmholtz instability, a fascinating fluid dynamic phenomenon that occurs when there is velocity shear in a single continuous fluid, or between two fluids.

## Theoretical Background
The Kelvin-Helmholtz instability is often visualized as billowing waves that appear at the interface between layers of fluid with different densities or velocities ! 

### Simulation Overview
The simulation models a two-dimensional fluid dynamics problem where two layers of fluid with different velocities interact, leading to the formation of characteristic wave-like structures. The simulation parameters include:

- **Domain Size:** 1x1 units, discretized into 128x128 grid points.
- **Initial Conditions:** Two layers with a velocity shear and a sinusoidal perturbation to initiate the instability.
- **Equation of State:** An ideal gas law with a specified adiabatic index (gamma).
- **Boundary Conditions:** Periodic in both the horizontal and vertical directions.

### Visualization
<p align="center">
  <img src="KHI.gif" width="300" alt="Shallow Water  Simulation Results for H=10m">
</p>
