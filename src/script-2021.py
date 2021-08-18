import pandas as pd
import numpy as np


visited_file = '../data/2021.xlsx'
#visited_file = '../data/data.xls'
df = pd.read_excel(visited_file, keep_default_na=False) #不包含默认缺失值
#df1 = df.iloc[7:12,1:11]  #读取电流、电压数据
#df1.columns = ['0.1c','c.1v','0.2c','0.2v','0.5c','0.5v','1c','1v','2c','2v']
#current = pd.series(pd.iloc())
# print(df.head())
# print(df.dtypes)
# shebei_df = df['仪器设备']
#print(df.head())
wtf = df['委托方']
je = df['金额']
#print(wtf.drop_duplicates()) #显示不含重复项的委托方名称
print(df[['委托方','金额']])
# 使用loc获取列子集
#subset = df.loc[:,[]]
#df1.to_csv('../output/data.csv', index=False)
#df2 = pd.read_csv('../output/data.csv',keep_default_na=False)
#print(df2)
#print(pd.read_csv('../output/data.csv',keep_default_na=False))



#scatter_plot