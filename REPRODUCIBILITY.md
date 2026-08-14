# Reproducibility notes

The canonical notebook was rebuilt from the original executed analysis notebook. Analytical model cells are retained; repository-specific modifications are restricted to runtime bootstrap, local structured paths, ZIP extraction, and the actual filename `lithology.shp` contained in the supplied archive.

## Why `data/reproducibility/` exists

The original analysis read public Google Sheets through the CSV (`gviz`) endpoint. The archived GRACE XLSX workbooks retain more floating-point precision than was exposed by the displayed Google-Sheets representation. In particular, the GRACE cells are formatted to 0.01 cm. The local GRACE CSVs therefore use 0.01-cm values and `MM/DD/YYYY` date headers to reproduce the original tabular representation.

The soil-moisture and benchmark CSVs are lossless CSV exports of the archived workbooks and allow the notebook to run without external data downloads.

## Original validation targets

The original executed notebook reported approximately:

- Imputation chronological holdout: R² 0.66, MAE 3.52 cm.
- Downscaling grouped-CV pooled OOF: R² 0.73, MAE 2.81 cm.
- Downscaling repeated strict outer tests: R² 0.61, MAE 3.60 cm.
- Final 2022–2023 temporal holdout: R² 0.70, MAE 3.18 cm.
- Balanced downscaling sample: 1,401 rows; 1,142 pre-2022 training rows; 259 holdout rows.

Small changes in numerical libraries can slightly change Random Forest tree construction and bootstrap intervals even with fixed seeds, so `requirements.txt` is pinned.
