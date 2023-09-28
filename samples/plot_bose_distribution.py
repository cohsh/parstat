#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

import parstat

def main():
    temperature = 300.0

    energy_max = 0.01

    energy = np.linspace(0.001, energy_max, 1000)

    n_bose = np.empty(0)

    for e in energy:
        n_bose = np.append(n_bose, parstat.bose_distribution(temperature, e))

    plt.plot(energy, n_bose, label="Bose Distribution")
    plt.xlabel("Energy ($\mathrm{Hartree}$)")
    plt.ylabel("Occupation Number")
    plt.legend()
    plt.savefig("test_bose_distribution.png")


if __name__ == "__main__":
    main()