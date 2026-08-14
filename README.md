# Bug River Area TWS Downscaling

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VytautasSam/bug_river_area_tws_downscaling/blob/main/GRACE_processing_pipeline.ipynb)

Colab-ready workflow for GRACE/GRACE-FO terrestrial water storage (TWS) gap reconstruction and bias-aware machine-learning downscaling from 0.25° to 0.1° in the Bug River Basin. The workflow includes hydroclimatic and physiographic predictors, Random Forest validation, mass-conservation correction, uncertainty analysis, and comparison with WGHM and GRACE-SeDA benchmark products.

## Repository structure

```text
bug_river_area_tws_downscaling/
├── GRACE_processing_pipeline.ipynb
├── README.md
├── REPRODUCIBILITY.md
├── requirements.txt
├── FILE_MANIFEST.json
├── SHA256SUMS.txt
├── data/
│   ├── spatial/
│   │   ├── dem.zip
│   │   ├── lithology.zip
│   │   ├── land_cover.zip
│   │   ├── land_cover_grid_PL_UA_BY.zip
│   │   └── grid_0.25.zip
│   ├── hydroclimate/
│   │   ├── 2013_2023_data.zip
│   │   ├── R_0.1.zip
│   │   ├── LST_ERA5.zip
│   │   └── SMS_GLDAS_025_2013-2023.xlsx
│   ├── grace/
│   │   ├── GRACE_025deg_orig.xlsx
│   │   └── GRACE_025deg_filled.xlsx
│   ├── benchmarks/
│   │   ├── WGHM_Bug_original.xlsx
│   │   ├── WGHM_Bug_01deg.xlsx
│   │   ├── GRACE_SeDA_Bug_original_05deg.xlsx
│   │   └── GRACE_SeDA_Bug_01deg.xlsx
│   ├── reproducibility/
│   │   ├── GRACE_025deg_orig.csv
│   │   ├── GRACE_025deg_filled.csv
│   │   ├── SMS_GLDAS_025_2013-2023.csv
│   │   ├── WGHM_Bug_original.csv
│   │   ├── WGHM_Bug_01deg.csv
│   │   ├── GRACE_SeDA_Bug_original_05deg.csv
│   │   └── GRACE_SeDA_Bug_01deg.csv
│   └── auxiliary/
│       ├── land_cover_grid.zip
│       └── raw_features_01_degree.zip
└── scripts/
    └── validate_inputs.py
```

## Run in Google Colab

Click **Open in Colab** above and run the notebook from the first cell. The notebook clones/synchronizes the `main` branch and installs `requirements.txt` before importing the analytical stack.

The canonical notebook intentionally requires the structured paths shown above. It does **not** search the repository root for data and contains no legacy `data/compat` fallback.

## Data organization

- `data/spatial/` — static geospatial grids and attributes.
- `data/hydroclimate/` — P/Q/ET, runoff, LST, and soil moisture inputs.
- `data/grace/` — archived original and filled GRACE workbooks.
- `data/benchmarks/` — WGHM and GRACE-SeDA products.
- `data/reproducibility/` — local CSV representations used by the analytical notebook to preserve the original tabular loading behavior.
- `data/auxiliary/` — supplied supporting datasets retained for provenance but not required by the canonical run.

## Validation

Before running the notebook, the repository can be checked locally with:

```bash
python scripts/validate_inputs.py
```

This verifies required files, expected ZIP contents, spreadsheet dimensions, and the GRACE 0.01-cm reproducibility representation.
