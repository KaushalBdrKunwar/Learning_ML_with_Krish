import pandas as pd
from io import StringIO

#Reading from url
url="https://www.fdic.gov/bank-failures/failed-bank-list"
df = pd.read_html(url)
print(df)