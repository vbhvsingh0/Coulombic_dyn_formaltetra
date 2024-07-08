# Coulombic_dyn_formaltetra

In this project, 100 initial conditions of formaldehyde tetra-cation generated with Harmonic-Wigner distribution were simulated using Coulombic forces. 
The code "simulation.py" simulates one single trajectory, given the initial atomic charges, initial geometry file (geom) and velocity file (veloc).

The code generates, 
a) output.txt : output file containing geometry, velocity, and energies at current time.
b) en.txt : energies at each time step written in a separate file.
c) coords.txt : coordinates of formaldehyde tetra-cation at each time-step.

The utility code 'projectveloc.py' projects the momenta of all the atoms along the bisector of C-Ds (See image below), and the axis perpendicular to it.

![image](https://github.com/vbhvsingh0/Coulombic_dyn_formaltetra/assets/157628979/4ab5a5ab-c07d-4fa2-9e0b-86f9e9d3276d)






