import numpy as np
import mlatom as ml
import ase
from ase.calculators.calculator import Calculator, all_changes
from ase.units import Hartree

class MLatomCalculator(Calculator):
    """
    ASE Calculator for AIQM & AIQM2 model using MLAtom

    Implements energy and force calculations with proper system change handling
    """
    implemented_properties = ['energy', 'forces']

    def __init__(self, charge=0, multiplicity=1, method='AIQM2'):
        """
        Initialize the AIQM2 Calculator

        Parameters:
        -----------
        charge : int, optional
            Molecular system charge (default: 0)
        multiplicity : int, optional
            Spin multiplicity (default: 1)
        method : str, optional
            mlatom method (default: 'AIQM2')

        Note)
        'aiqm2': ['AIQM2', 'AIQM2@DFT']
        'torchani': [
          "ANI-1x", "ANI-1ccx", "ANI-2x", 'ANI-1x-D4',
          'ANI-2x-D4', 'ANI-1xnr', 'ANI-1ccx-gelu',
          'ANI-1ccx-gelu-D4', 'ANI-1x-gelu', 'ANI-1x-gelu-d4'
          ]
        """
        super().__init__()
        self.charge = charge
        self.multiplicity = multiplicity
        self._model = ml.models.methods(method=method)
        self.molecule = None

    def _convert_mlatom_molecule(self, atoms:ase.Atoms):
        """Convert ASE Atoms to MLAtom molecule"""

        molecule = ml.data.molecule(
            charge=self.charge,
            multiplicity=self.multiplicity
        ).read_from_numpy(
            coordinates=self.atoms.positions,
            species=np.array(self.atoms.symbols)
        )
        self.molecule = molecule

    def calculate(self, atoms=None, properties=None, system_changes=all_changes):
        """
        Calculate energy and forces for the system

        Parameters:
        -----------
        atoms : ase.Atoms
            Atoms object to calculate
        properties : list
            Properties to calculate
        system_changes : list
            List of system changes
        """
        # Apply standard Calculator checks for system changes
        if properties is None:
            properties = self.implemented_properties

        super().calculate(atoms, properties, system_changes)

        # mlatom molecule object
        self._convert_mlatom_molecule(atoms)

        # calculate energy and gradients
        self._model.predict(
            molecule=self.molecule,
            calculate_energy=True if 'energy' in properties else False,
            calculate_energy_gradients=True if 'forces' in properties else False
        )

        # unit conversion
        # energy : Ha => eV
        # forces : Ha/Ang => eV/Ang
        self.results['energy'] = self.molecule.energy * Hartree
        self.results['forces'] = - self.molecule.energy_gradients * Hartree