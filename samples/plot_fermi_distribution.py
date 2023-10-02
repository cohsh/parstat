#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

import parstat

def main():
    energy_max = 0.01

    energy = np.linspace(-energy_max, energy_max, 10000)

    for i in range(5):
        temperature = i * 100.0
        n_fermi = parstat.fermi_distribution(temperature, energy)
        plt.plot(energy, n_fermi, label="{0} K".format(int(temperature)))

    plt.title("Fermi Distribution")
    plt.xlabel("Energy ($\mathrm{Hartree}$)")
    plt.ylabel("Occupation Number")
    plt.legend()
    plt.savefig("test_fermi_distribution.png")


if __name__ == "__main__":
    main()