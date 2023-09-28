#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

import parstat

def main():
    temperature = 300.0

    energy_max = 0.01

    energy = np.linspace(-energy_max, energy_max, 1000)

    n_fermi = np.empty(0)

    for e in energy:
        n_fermi = np.append(n_fermi, parstat.fermi_distribution(temperature, e))

    plt.plot(energy, n_fermi, label="Fermi Distribution")
    plt.xlabel("Energy ($\mathrm{Hartree}$)")
    plt.ylabel("Occupation Number")
    plt.legend()
    plt.savefig("test_fermi_distribution.png")


if __name__ == "__main__":
    main()