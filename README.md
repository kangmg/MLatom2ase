# MLatom2ase
MLatom Calculator for ASE Interface

## Installation

> pip
```shell
pip install git+https://github.com/kangmg/MLatom2ase.git
```

## Usage

```python
from mlatom2ase import MLatomCalculator
from ase.build import molecule

atoms = molecule('H2O')

calc = MLatomCalculator(charge=0, multiplicity=1, method='AIQM2')
atoms.calc = calc
energy = atoms.get_potential_energy()

print(f"AIQM2 Energy : {energy} eV")
```
