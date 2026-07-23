"""
run_nep89.py — run in mlip-nep89 environment
conda activate mlip-nep89
"""

import sys
import time
import numpy as np
from ase.io import read
from calorine.calculators import CPUNEP

# argv[1]: path to cached dft relaxation energies
# argv[2]: path to write mlip single-point prediction to
# argv[3]: device type — unused, CPUNEP is CPU-only (kept for arg parity with mace script)
# argv[4]: "1" to print per-point timing, "0" to stay quiet

show_timing = len(sys.argv) > 4 and sys.argv[4] == "1"

MODEL = "/Users/zschwab/models/nep89.txt"

ads_system = read(sys.argv[1], index=":")

calc = CPUNEP(MODEL)

for atoms in ads_system:
    atoms.calc = calc

energies_list = []
forces_list = []
times_list = []

for i, atoms in enumerate(ads_system):
    t0 = time.perf_counter()
    e = atoms.get_potential_energy()
    f = atoms.get_forces()
    dt = time.perf_counter() - t0

    energies_list.append(e)
    forces_list.append(f)
    times_list.append(dt)

    if show_timing:
        print(f"  point {i}: {dt:.3f}s")

np.savez(
    sys.argv[2],
    mlip_energies=np.array(energies_list),
    mlip_forces=np.array(forces_list),
    point_times=np.array(times_list),
)