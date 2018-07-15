#!/usr/bin/python
#-*- Doding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

df = pd.read_csv("./takahashi/bigdata/all_data.csv", engine="python")
rain = pd.read_csv("./takahashi/rains/all_rain_data.csv", engine="python")

rain["年月日時"] = pd.to_datetime(rain["年月日時"])
df["年月日時"] = pd.to_datetime(df["年月日時"])

df = df.set_index("年月日時")
rain = rain.set_index("年月日時")




print(df)
# y1 = range(0, 24, 1)
# x1 = pd.date_range('2018-06-14 00:00:00', periods=24, freq='D')
# ax.plot(x1, y1)
plt.plot(df.index, df["水位"])
plt.plot(rain.index, rain["降水量(mm)"])
plt.show()
