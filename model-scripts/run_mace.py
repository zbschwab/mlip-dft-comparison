"""
run_mace.py — run in mlip-mace environment
conda activate mlip-mace
"""

import sys
import numpy as np
from ase.io import read
from mace.calculators import mace_mp

# print("hello from mace!")  # check connection

# argv[1]: path to cached dft relaxation energies
# argv[2]: path to write mlip single-point prediction to
# argv[3]: device type ("cpu", "cuda", "mps")

ads_system = read(sys.argv[1], index=":")

calc = mace_mp(model="medium", dispersion=False, default_dtype="float32", device=sys.argv[3])

for atoms in ads_system:
    atoms.calc = calc

energies_list = []
forces_list = []

for atoms in ads_system:
    energies_list.append(atoms.get_potential_energy())
    forces_list.append(atoms.get_forces())

np.savez(
    sys.argv[2],
    mlip_energies=np.array(energies_list),
    mlip_forces=np.array(forces_list)
)
