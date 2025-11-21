import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import matplotlib.font_manager as font_manager

system = platform.system()
if system == "Windows":
    font_path = "C:/Windows/Fonts/malgun.ttf"
elif system == "Darwin":
    font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
elif system == "Linux":
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
else:
    font_path = None

if font_path:
    font = font_manager.FontProperties(fname=font_path).get_name()
    plt.rcParams['font.family'] = font
    plt.rcParams['axes.unicode_minus'] = False
else:
    print("폰트 경로를 확인해주세요.")

# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# print("type(x):", type(x))
# print("type(y):", type(y))
# print("x:", x)
# print("y:", y)

# plt.figure(figsize=(10, 5))
# plt.plot(x, y)
# plt.title("Sine Wave")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

data = [10, 11, 33, 22, 55]
data2 = [10, 20, 30, 40, 50]
data3 = [5, 10, 15, 20, 25]
# plt.plot(data)
# plt.figure()
# plt.plot(data2)
# plt.figure(1)
# plt.plot(data3)
# plt.title("Data")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
