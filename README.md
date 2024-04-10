# 1. 2D Shallow Water Simulation

## Introduction
Welcome to the 2D Shallow Water Simulation project! This repository contains a numerical simulation designed to solve the 2D shallow water equations using finite differences. By modeling the momentum equations linearly and solving the continuity equation in its nonlinear form, this project provides insights into fluid dynamics in shallow water contexts under various conditions.

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

## Experimental Setup
The simulation was executed five times to explore the dynamics under different conditions. The simulation produced videos that visualize the surface elevation and velocity field! 
1. Water depth of H = 10 meters, with Coriolis effect.
2. Water depth of H = 10 meters, without Coriolis effect.
3. Water depth of H = 100 meters, with Coriolis effect.
4. Water depth of H = 100 meters, without Coriolis effect.
5. Water depth of H = 4000 meters, with Coriolis effect.

