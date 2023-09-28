import sys
import numpy as np

float_min = sys.float_info.min
float_max = sys.float_info.max

def boltzmann_distribution(temperature: float, energy: float) -> float:
    # Calculates the occupation number of particles that follow the Blotzmann distribution.

    kbt = temperature * 3.167e-6  # Kelvin -> Hartree
    n = 0.0

    if kbt > float_min:
        beta = 1.0 / kbt  # inverse temperature
        x = beta * energy
        n = np.exp(-x)
        if n == np.inf:
            n = float_max
    else:
        if energy > 0.0:
            n = 0.0
        elif energy == 0.0:
            n = 1.0
        else:
            n = float_max
    return n

def fermi_distribution(temperature: float, energy: float) -> float:
    # Calculates the occupation number of particles that follow the Fermi-Dirac distribution.

    boltzmann_factor = boltzmann_distribution(temperature, energy)
    n = 0.0
    n = boltzmann_factor / (1.0 + boltzmann_factor)
    return n

def bose_distribution(temperature: float, energy: float) -> float:
    # Calculates the occupation number of particles that follow the Bose-Einstein distribution.

    boltzmann_factor = boltzmann_distribution(temperature, energy)
    if boltzmann_factor != 1.0:
        n = boltzmann_factor / (1.0 - boltzmann_factor)
    else:
        n = float_max
    return n

def gaussian_distribution(sigma: float, energy: float) -> float:
    # Calculates the occupation number of particles that follow the Gaussian distribution.

    n = np.exp(- energy ** 2 / (2.0 * sigma ** 2)) / (np.sqrt(2.0 * np.pi) * sigma)
    return n