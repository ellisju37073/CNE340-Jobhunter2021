import pandas

tables = pandas.read_excel ('https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2DXL0_PTE_R5XCA_DPGw.xls', sheet_name='Data 1',
                            header = 2, index_col='Date')
tables.rename(columns = {'Weekly West Coast (PADD 5) Except California No 2 Diesel Ultra Low Sulfur (0-15 ppm) Retail Prices  (Dollars per Gallon)'
                         :'Diesel_Price'}, inplace=True)
print(tables)