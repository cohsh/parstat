#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

import parstat

def main():
    energy_max = 0.01
    sigma = 0.001

    energy = np.linspace(-energy_max, energy_max, 1000)

    n_gaussian = np.empty(0)

    for e in energy:
        n_gaussian = np.append(n_gaussian, parstat.gaussian_distribution(sigma, e))

    plt.plot(energy, n_gaussian, label="Gaussian Distribution")
    plt.xlabel("Energy ($\mathrm{Hartree}$)")
    plt.ylabel("Occupation Number")
    plt.legend()
    plt.savefig("test_gaussian_distribution.png")


if __name__ == "__main__":
    main()