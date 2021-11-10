

import requests
import pandas as pd

url = "https://finance.yahoo.com/quote/LOMLF/history?p=LOMLF"

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}

lion= requests.get(url, headers=header)

dfs_lion = pd.read_html(lion.text, header = 0)

return_table=dfs_lion[0]

print(return_table)