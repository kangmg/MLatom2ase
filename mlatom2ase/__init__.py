__version__ = '0.0.1'

from .ase_interface import MLatomCalculator

# ---------- check $dft4bin ---------- #

import subprocess
import warnings
import os

def dft4binChecker():
    """check if dft4 is installed
    """
    try:
        return True if subprocess.run(['dft4', '--version']).returncode == 0 else False
    except FileNotFoundError:
        warnings.warn(
            'dft4 is not found.\nPlease install first.',
            category=UserWarning
            )
        return False

def envChecker():
    dftd4bin = os.environ.get('dftd4bin')
    if not dftd4bin:
        warnings.warn(
            '$dft4bin is not found.\nPlease set the environment variable: export dftd4bin=/path/to/dft4bin',
            category=UserWarning
            )
        return False
    return True

warnings.simplefilter('always', UserWarning)

dft4binChecker()
envChecker()

# ------------------------------------ #
