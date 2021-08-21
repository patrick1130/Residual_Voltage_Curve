import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# visited_file = '../data/2021.xlsx'
visited_file = '../data/data.xls'
df = pd.read_excel(visited_file)
df1c = df.iloc[7:12, 1:2]
df1v = df.iloc[7:12, 2:3]
df2c = df.iloc[7:12, 3:4]
df2v = df.iloc[7:12, 4:5]
df3c = df.iloc[7:12, 5:6]
df3v = df.iloc[7:12, 6:7]
df4c = df.iloc[7:12, 7:8]
df4v = df.iloc[7:12, 8:9]
df5c = df.iloc[7:12, 9:10]
df5v = df.iloc[7:12, 10:11]
df1c.columns = ['1']
df2c.columns = ['1']
df3c.columns = ['1']
df4c.columns = ['1']
df5c.columns = ['1']
df1v.columns = ['2']
df2v.columns = ['2']
df3v.columns = ['2']
df4v.columns = ['2']
df5v.columns = ['2']
# 连接行数据
current_concat = pd.concat([df1c, df2c, df3c, df4c, df5c], join='inner')
voltage_concat = pd.concat([df1v, df2v, df3v, df4v, df5v], join='inner')
# 删除NA值
df1 = current_concat.dropna()
df2 = voltage_concat.dropna()
# 重置索引
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)

dd1 = df1.abs()  # 取绝对值
dd2 = df2.abs()

# print(dd1)
# print(dd2)
# df1.columns = ['1c','1v','2c','2v','3c','3v','4c','4v','5c','5v'

# current_concat.to_csv('../output/data.csv', index=False)
# df2 = pd.read_csv('../output/data.csv',keep_default_na=False)
# print(df2)
# print(pd.read_csv('../output/data.csv',keep_default_na=False))
# x=np.linspace(0.05,10,1000)
# y=np.random.rand(1000)

# z = np.polyfit(x, y, 2)  # np.polyfit(x,y,deg=1) 返回多项式系数
# a = np.poly1d(z)  # 生成方程式
# plt.plot(x, a(x))  # 拟合曲线

# plt.scatter(dd1,dd2)

# plt.legend()
# plt.show()
