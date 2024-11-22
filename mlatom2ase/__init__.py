__version__ = '0.0.1'

# ---------- check $dft4bin ---------- #
import subprocess
import warnings
from .ase_interface import MLatomCalculator

def dft4binChecker():
  """check if dft4 is installed
  """
  try:
    return True if subprocess.run(['dft4', '--version']).returncode == 0 else False
  except FileNotFoundError:
    return False

# ------------------------------------ #

if not dft4binChecker():
    warnings.warn(
        '$dft4bin is not found.\nPlease set the environment variable: export dftd4bin=/path/to/dft4bin',
        category=ImportWarning
    )
