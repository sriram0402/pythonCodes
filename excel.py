from openpyxl import load_workbook
import pandas as pd
wb=pd.read_excel('Format.xlsx')
print(wb.head())
for i in wb:
    print(i)
