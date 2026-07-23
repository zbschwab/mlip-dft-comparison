"""
run_mattersim.py — run in mlip-mattersim environment
conda activate mlip-mattersim
"""

import sys
import numpy as np
from ase.io import read
from mattersim.forcefield import MatterSimCalculator

# print("hello from mattersim!")  # check connection

# argv[1]: path to cached dft relaxation energies
# argv[2]: path to write mlip signle-point prediction to
# argv[3]: device type ("cpu", "cuda", "mps")

ads_frames = read(sys.argv[1], index=":")

calc = MatterSimCalculator(device=sys.argv[3])

for atoms in ads_frames:
    atoms.calc = calc

energies_list = []
forces_list = []

for atoms in ads_frames:
    energies_list.append(atoms.get_potential_energy())
    forces_list.append(atoms.get_forces())

np.savez(
    sys.argv[2],
    mlip_energies=np.array(energies_list),
    mlip_forces=np.array(forces_list)
)
