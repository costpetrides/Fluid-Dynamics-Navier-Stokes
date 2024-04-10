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
The simulation was executed five times to explore the dynamics under different conditions. The simulation produced videos that visualize the surface elevation and velocity field! 
1. Water depth of H = 10 meters, with Coriolis effect.
2. Water depth of H = 10 meters, without Coriolis effect.
3. Water depth of H = 100 meters, with Coriolis effect.
4. Water depth of H = 100 meters, without Coriolis effect.
5. Water depth of H = 4000 meters, with Coriolis effect.

<p align="center">
  <img src="https://github.com/costpetrides/Fluid-Dynamics/blob/main/Figures/H10.png" width="600" alt="Shallow Water  Simulation Results for H=10m">
</p>



Creating a README for a Kelvin-Helmholtz instability simulation involves explaining the physical phenomenon, describing the code's functionality, and guiding users on how to run the simulation. Let's draft a comprehensive README to encapsulate your project effectively.

---

# 2. Kelvin-Helmholtz Instability Simulation

## Introduction
Welcome to the Kelvin-Helmholtz Instability Simulation project! This repository contains a Python script designed to simulate the Kelvin-Helmholtz instability, a fascinating fluid dynamic phenomenon that occurs when there is velocity shear in a single continuous fluid, or between two fluids.

## Theoretical Background
The Kelvin-Helmholtz instability is often visualized as billowing waves that appear at the interface between layers of fluid with different densities or velocities. This instability is crucial for understanding mixing processes in both atmospheric sciences and astrophysics.

### Simulation Overview
The simulation models a two-dimensional fluid dynamics problem where two layers of fluid with different velocities interact, leading to the formation of characteristic wave-like structures. The simulation parameters include:

- **Domain Size:** 1x1 units, discretized into 128x128 grid points.
- **Initial Conditions:** Two layers with a velocity shear and a sinusoidal perturbation to initiate the instability.
- **Equation of State:** An ideal gas law with a specified adiabatic index (gamma).
- **Boundary Conditions:** Periodic in both the horizontal and vertical directions.

## Running the Simulation
Ensure you have Python installed along with NumPy and Matplotlib libraries. Clone this repository, navigate to the project directory, and execute the Kelvin-Helmholtz simulation script:

```bash
python kelvin_helmholtz_simulation.py
```

The script will advance through time steps, updating the fluid's density, velocity, and pressure fields based on the solver's computations. It periodically outputs visualizations of the density field to show the development of the Kelvin-Helmholtz instability.

### Visualization
The simulation's output is visualized using Matplotlib, showing the evolution of the fluid's density field over time. This visualization helps illustrate the dynamic nature of the Kelvin-Helmholtz waves and their growth.

## Contributing
Contributions to this project are welcome! Whether it's enhancing the simulation's accuracy, extending its capabilities, or improving documentation, your input is valued. Please feel free to fork the repository and submit pull requests.

## License
This project is released under [SPECIFY LICENSE], facilitating collaboration and distribution.

---

This README provides a structured overview, introducing the Kelvin-Helmholtz instability, detailing the simulation's scope, and guiding users on how to run and interact with your code. Remember to replace `[SPECIFY LICENSE]` with the actual license under which your project is released, and feel free to adjust any section as necessary to better match your project's specifics.
