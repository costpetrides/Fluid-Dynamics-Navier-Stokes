# 1. 2D Shallow Water Simulation

## Introduction
Welcome to the 2D Shallow Water Simulation project! This repository contains a numerical simulation designed to solve the 2D shallow water equations using finite differences. By modeling the momentum equations linearly and solving the continuity equation in its nonlinear form, this project provides insights into fluid dynamics in shallow water contexts under various conditions, so fell free to play with different initial conditions and senarios ! 

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
1. Water depth of H = 10 meters, with Coriolis effect and without Coriolis effect. [H=10m Video](https://drive.google.com/file/d/1YR8FDIVf6ByGHbSNfJscaeu65GOWXCBM/view?usp=sharing)
2. Water depth of H = 100 meters, with Coriolis effect and without Coriolis effect. [H=100m Video]

<p align="center">
  <a href="https://drive.google.com/file/d/1YR8FDIVf6ByGHbSNfJscaeu65GOWXCBM/view?usp=sharing" target="_blank">
    <img src="https://github.com/costpetrides/Fluid-Dynamics/blob/main/Figures/H10.png" width="600" alt="Shallow Water  Simulation Results for H=10m">
  </a>
</p>

---

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
  <img src="https://github.com/costpetrides/Fluid-Dynamics/blob/main/Figures/KHI.png" width="300" alt="Shallow Water  Simulation Results for H=10m">
</p>
