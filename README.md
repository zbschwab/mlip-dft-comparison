# Project README

## Overview
This notebook compares MLIP-predicted energies and forces against DFT reference calculations. For each frame in a DFT trajectory, the MLIP takes the DFT-computed structure (atomic positions, cell) as input and performs a single-point evaluation, predicting E and F(r) for that fixed, pre-relaxed geometry. 

This is used to find adsorption energy (E_ads = E_tot − E_slab − E_gas).

## DFT Data
Download DFT runs from Box or DropBox and drop the unzipped folders into `dft-data/`. (A good starting point is [COOH_on_YO4PdCu](https://app.box.com/folder/386914302449)) \
Note that DFT runs with no OUTCAR (FastRelax/OUTCAR doesn't count) and multiple OUTCARs (takes unreasonably long to run with this notebook) are invalid data here.

## Conda Environment Setup

This project uses one primary Conda environment for the notebook and several model-specific environments for ML models with incompatible dependencies.

### 1. Create the primary environment

From the repository root:

```bash
conda env create -f model-scripts/conda_envs/mlip.yml
```

### 2. Create the model environments

From the repository root (for each model you want to run):
```bash
conda env create -f model-scripts/conda-envs/mlip-mace.yml
conda env create -f model-scripts/conda-envs/mlip-mattersim.yml
conda env create -f model-scripts/conda-envs/mlip-uma.yml
conda env create -f model-scripts/conda-envs/mlip-nep89.yml
```
**Note on NEP89:** To run this model, you must download `nep89.txt` (found [here](https://zenodo.org/records/21285022)) and place the filepath to this in the `model-scripts/run_nep89.py` script.

### 3. Verify installation

```bash
conda env list
```

You should see:

```text
mlip
mlip-mace
mlip-mattersim
mlip-uma
mlip-nep89
```

### 4. Run the notebook

Activate your primary notebook environment:

```bash
conda activate mlip
```

The notebook will automatically invoke model scripts using the appropriate Conda environment.

### Troubleshooting Conda Env Setup

* Do not rename the Conda environments; notebook scripts expect the names defined in the YAML files.
* If environment creation fails, remove the environment and recreate it:

```bash
conda env remove -n <environment_name>
conda env create -f <yml_file>
```
