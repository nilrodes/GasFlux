# EK80 Gas Flux and Bubble Radius Analysis

This archive contains two Jupyter notebooks for acoustic analysis of gas seepage using EK80 echosounder data:

- `notebooks/BubbleRadius.ipynb` — broadband target-strength processing and bubble-radius estimation.
- `notebooks/GasFlux.ipynb` — calibrated volume-backscattering processing, gas-flux calculations, plots, statistics, and Excel export.

## 1. Requirements

The Conda environment is defined in `environment.yml`. Create and activate it with:

```bash
conda env create -f environment.yml
conda activate gasflux
```

Launch Jupyter from the project root directory:

```bash
jupyter lab
```

The notebooks import `project_config.py` from the project root, so running Jupyter from the root directory is recommended.

## 2. Input data

The raw echosounder recordings, calibration XML, and CTD profile are not distributed with this code archive. Obtain the data through the relevant project data-access route and place authorized copies in `data/`. Do not include data in a public release unless you have permission to redistribute them.

Expected filenames are configured in `project_config.py`:

- `bubble_radius.raw` — input for the bubble-radius notebook.
- `gas_flux_conversion.raw` — raw file used in the initial RAW-to-NetCDF conversion cell.
- `gas_flux_analysis.raw` — raw file used for calibrated Sv/TS analysis.
- `calibration.xml` — EK80 calibration XML.
- `ctd_profile.csv` — CTD profile CSV.

Edit the filenames or paths in `project_config.py` to match your available data. The CTD CSV is expected to have column names in the first row and units in the second row; it must include `Temperature` and `Salinity` columns. Review `mean_depth` in the notebook and set it to the appropriate site depth.

## 3. Run order

1. Open the notebook from `notebooks/`.
2. Run cells from top to bottom.
3. Check the parameters and thresholds in the notebook against the manuscript methods before interpreting the results.
4. `GasFlux.ipynb` writes the Excel summary to `outputs/EK80_Gas_Flux_Full_Summary.xlsx`. Converted NetCDF files are also written to `outputs/`.

## 4. Reproducibility and scientific cautions

- These notebooks have been made portable by removing user-specific absolute paths and Windows-specific temporary directories.
- The archive does not include the source recordings, calibration file, or CTD data; therefore the full workflow cannot be verified without access to those inputs.
- The notebooks contain empirical thresholds and physical parameters. Verify their values, units, assumptions, and correspondence to the manuscript before publication. Path cleanup is not scientific validation of the calculation methods.
- The notebooks have had saved cell outputs removed so that machine-specific paths and stale outputs are not inadvertently distributed. Re-run the notebooks to regenerate outputs.
- This environment file declares the direct analysis dependencies rather than every transitive package in the original local environment. For strict long-term reproducibility, create and archive a tested lockfile after validating the environment on the target operating system.

## 5. Output directory

Generated NetCDF and Excel files are written to `outputs/`. This directory is intentionally empty in the source archive.

## 6. Citation and license

Please cite the associated manuscript when using this code. A software license has not been assigned because the copyright holder and intended reuse terms have not yet been confirmed. Select and add a license before publicly releasing the archive.
