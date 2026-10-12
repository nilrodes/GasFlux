"""Portable paths and filenames for the gas-flux supplementary project.

Place input data in the ./data directory, or edit the filenames below.
Run Jupyter from the project root so these relative paths resolve consistently.
"""
from pathlib import Path

PROJECT_ROOT = Path.cwd().resolve()
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Edit these filenames to match the data files available to you.
BUBBLE_RADIUS_RAW_FILE = DATA_DIR / "bubble_radius.raw"
GAS_FLUX_CONVERSION_RAW_FILE = DATA_DIR / "gas_flux_conversion.raw"
GAS_FLUX_ANALYSIS_RAW_FILE = DATA_DIR / "gas_flux_analysis.raw"
CALIBRATION_XML_FILE = DATA_DIR / "calibration.xml"
CTD_PROFILE_CSV_FILE = DATA_DIR / "ctd_profile.csv"
