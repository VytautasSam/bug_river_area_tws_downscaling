from pathlib import Path
import sys
import zipfile
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'data'

REQUIRED = {
    'spatial/dem.zip',
    'spatial/lithology.zip',
    'spatial/land_cover.zip',
    'spatial/land_cover_grid_PL_UA_BY.zip',
    'spatial/grid_0.25.zip',
    'hydroclimate/2013_2023_data.zip',
    'hydroclimate/R_0.1.zip',
    'hydroclimate/LST_ERA5.zip',
    'hydroclimate/SMS_GLDAS_025_2013-2023.xlsx',
    'grace/GRACE_025deg_orig.xlsx',
    'grace/GRACE_025deg_filled.xlsx',
    'benchmarks/WGHM_Bug_original.xlsx',
    'benchmarks/WGHM_Bug_01deg.xlsx',
    'benchmarks/GRACE_SeDA_Bug_original_05deg.xlsx',
    'benchmarks/GRACE_SeDA_Bug_01deg.xlsx',
    'reproducibility/GRACE_025deg_orig.csv',
    'reproducibility/GRACE_025deg_filled.csv',
    'reproducibility/SMS_GLDAS_025_2013-2023.csv',
    'reproducibility/WGHM_Bug_original.csv',
    'reproducibility/WGHM_Bug_01deg.csv',
    'reproducibility/GRACE_SeDA_Bug_original_05deg.csv',
    'reproducibility/GRACE_SeDA_Bug_01deg.csv',
}

missing = sorted(rel for rel in REQUIRED if not (D / rel).is_file())
if missing:
    raise SystemExit('Missing files:\n  ' + '\n  '.join(missing))


def zip_names(rel):
    with zipfile.ZipFile(D / rel) as z:
        return {Path(n).name for n in z.namelist() if n and not n.endswith('/')}

assert 'dem.shp' in zip_names('spatial/dem.zip')
assert 'lithology.shp' in zip_names('spatial/lithology.zip')
assert 'land_cover_grid_PL_UA_BY.shp' in zip_names('spatial/land_cover_grid_PL_UA_BY.zip')
assert 'grid_0.25.shp' in zip_names('spatial/grid_0.25.zip')

hydro = zip_names('hydroclimate/2013_2023_data.zip')
assert all(f'{year}_data.shp' in hydro for year in range(2013, 2024))
runoff = zip_names('hydroclimate/R_0.1.zip')
assert all(f'R_{year}.shp' in runoff for year in range(2013, 2024))
lst = zip_names('hydroclimate/LST_ERA5.zip')
assert all(f'LST_{year}.shp' in lst for year in range(2013, 2024))

orig = pd.read_csv(D / 'reproducibility/GRACE_025deg_orig.csv')
filled = pd.read_csv(D / 'reproducibility/GRACE_025deg_filled.csv')
sm = pd.read_csv(D / 'reproducibility/SMS_GLDAS_025_2013-2023.csv')
assert orig.shape == (119, 241), orig.shape
assert filled.shape == (119, 135), filled.shape
assert sm.shape == (119, 133), sm.shape
assert list(orig.columns[:3]) == ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2']
assert list(filled.columns[:3]) == ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2']

for frame, name in [(orig, 'GRACE original'), (filled, 'GRACE filled')]:
    values = frame.iloc[:, 3:].apply(pd.to_numeric, errors='coerce').to_numpy(dtype=float)
    finite = values[np.isfinite(values)]
    if not np.allclose(finite * 100, np.round(finite * 100), atol=1e-8):
        raise AssertionError(f'{name} is not at 0.01-cm source precision')

print('PASS: structured repository inputs are complete and internally consistent.')
print(f'Primary/reproducibility inputs checked: {len(REQUIRED)}')
print('GRACE original:', orig.shape, '| GRACE filled:', filled.shape, '| Soil moisture:', sm.shape)
