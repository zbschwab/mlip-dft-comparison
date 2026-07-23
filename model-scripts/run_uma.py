"""
run_mattersim.py — run in mlip-mattersim environment
conda activate mlip-mattersim
"""

import sys
import numpy as np
from ase.io import read
from fairchem.core import pretrained_mlip, FAIRChemCalculator

# print("hello from uma!")  # check connection

# argv[1]: path to cached dft relaxation energies
# argv[2]: path to write mlip signle-point prediction to
# argv[3]: device type ("cpu", "cuda", "mps")

ads_frames = read(sys.argv[1], index=":")

predictor = pretrained_mlip.get_predict_unit(
    "uma-s-1p2", device=sys.argv[3]
)

calc = FAIRChemCalculator(predictor, task_name="oc20", seed=None)

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
