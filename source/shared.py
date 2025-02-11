from pathlib import Path

import pandas as pd
import geopandas as gpd

app_dir = Path(__file__).parent
df = pd.read_csv(app_dir / "EM-DAT.csv")

"""
indo = pd.read_csv()
province = gpd.read_file('')
regency = gpd.read_file('')
district = gpd.read_file('')

"""