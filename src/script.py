import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

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
df1c.columns = ['current']
df2c.columns = ['current']
df3c.columns = ['current']
df4c.columns = ['current']
df5c.columns = ['current']
df1v.columns = ['voltage']
df2v.columns = ['voltage']
df3v.columns = ['voltage']
df4v.columns = ['voltage']
df5v.columns = ['voltage']
# 连接行数据
current_concat = pd.concat([df1c, df2c, df3c, df4c, df5c], join='inner')
voltage_concat = pd.concat([df1v, df2v, df3v, df4v, df5v], join='inner')
# 删除NA值
df1 = current_concat.dropna()
df2 = voltage_concat.dropna()
# 重置索引
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
# 取绝对值
dd1 = df1.abs()
dd2 = df2.abs()
# 合并最终数据表
zz = pd.concat([dd1, dd2], axis=1)
# 转为数值型
zz = zz.astype(float)
# print(zz.dtypes)
x = zz['current']
y = zz['voltage']

# print(zz)
# currents = sns.load_dataset('tips')
# print(currents.head())
'''
#最小二乘法线性回归
model = smf.ols(formula='voltage ~ current',data=zz)
results=model.fit()
y_pred = results.predict(x)
fig=plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,y)
ax.plot(x,y_pred)
plt.show()
'''

# print(results.summary())#回归结果

# print(results.params)#回归系数


# print(dd1)
# print(dd2)
# df1.columns = ['1c','1v','2c','2v','3c','3v','4c','4v','5c','5v'

# current_concat.to_csv('../output/data.csv', index=False)
# df2 = pd.read_csv('../output/data.csv',keep_default_na=False)
# print(df2)
# print(pd.read_csv('../output/data.csv',keep_default_na=False))
# x=np.linspace(0.05,10,1000)
# y=np.random.rand(1000)
# x=results.params['current']
# y=results.params['Intercept']


# np.polyfit(x,y,deg=1) 返回多项式系数
z = np.polyfit(x, y, deg=2)
a = np.poly1d(z)  # 生成方程式
plt.plot(x, a(x),"r--")  # 拟合曲线

plt.scatter(x, y)

print("y=%.6fx\u00B2+%.6fx+%.6f"%(z[0],z[1],z[2]))#'\u00B2'代表 2（上标）
plt.legend()
plt.show()
