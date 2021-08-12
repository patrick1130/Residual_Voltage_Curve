import pandas as pd
import xlwt  # 处理.xls
import openpyxl  # 处理.xlsx

df = pd.read_excel('../data/data.xls')
# print(df.head())
# print(df.dtypes)
# shebei_df = df['仪器设备']
# print(df.iloc[4])

# 使用loc获取列子集
#subset = df.loc[:,[]]

print(df.iloc[6:12,1:11])
