#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

import parstat

def main():
    energy_min = 0.001
    energy_max = 0.01

    energy = np.linspace(energy_min, energy_max, 1000)

    for i in range(5):
        temperature = i * 100.0
        n_bose = np.empty(0)
        for e in energy:
            n_bose = np.append(n_bose, parstat.bose_distribution(temperature, e))

        plt.plot(energy, n_bose, label="{0} K".format(int(temperature)))
    
    plt.title("Bose Distribution")
    plt.xlabel("Energy ($\mathrm{Hartree}$)")
    plt.ylabel("Occupation Number")
    plt.legend()
    plt.savefig("test_bose_distribution.png")


if __name__ == "__main__":
    main()