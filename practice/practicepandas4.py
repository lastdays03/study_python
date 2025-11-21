import pandas as pd
import numpy as np
import os

# 경로 조회
print("경로 조회:", os.getcwd())

df_rain = pd.read_csv("data/sea_rain1.csv", encoding="utf-8")
print("df_rain:\n", df_rain)

df_rain.to_csv("data/sea_rain1_result.csv", encoding="utf-8", index=False)
df_rain.to_excel("data/sea_rain1_result.xlsx", index=False)
df_rain.to_json("data/sea_rain1_result.json", orient="records", lines=True, force_ascii=False)

df_rain2 = pd.read_json("data/sea_rain1_result.json", orient="records", lines=True)
print("df_rain2:\n", df_rain2)

df_rain3 = pd.read_excel("data/sea_rain1_result.xlsx")
print("df_rain3:\n", df_rain3)
