from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport

root = Path(__file__).resolve().parents[1]
source = root / "data" / "raw" / "online_retail_II.xlsx"
report = root / "reports" / "data_profile.html"

df = pd.read_excel(
    source,
    sheet_name="Year 2010-2011",
    nrows=100_000,
    dtype={"Invoice": str, "StockCode": str},
)

report.parent.mkdir(parents=True, exist_ok=True)
ProfileReport(df, title="Online Retail II", minimal=True).to_file(str(report))