import pandas as pd
import xlwt #处理.xls
import openpyxl #处理.xlsx

df = pd.read_excel('../data/data.xls')
print(df.head())



