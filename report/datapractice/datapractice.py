import platform
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import numpy as np
import os

# 1. 폰트 설정
# 운영체제에 따른 한글 폰트 설정
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
    mpl.rcParams['font.family'] = font
else:
    print("폰트 경로를 확인해주세요.")

# 마이너스 부호 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

# 현재 작업 경로 출력
print("Current Working Directory:", os.getcwd())

# 2. 데이터 로드 및 전처리
# pip install openpyxl xlrd (xls, xlsx 파일 사용을 위해 필요)
# 엑셀 파일 읽기
d1 = pd.read_excel("report/datapractice/notExercise.xls")

# 데이터 분리
# '대분류'와 '분류'가 다른 경우 (구별 데이터 등)
d2 = d1[d1['대분류'] != d1['분류']]

# '대분류'와 '분류'가 같은 경우 (서울시 전체 통계 등) -> '지역분류'로 이름 변경
d3 = d1[d1['대분류'] == d1['분류']]
d3.loc[:, '대분류'] = '지역분류'

# '대분류'를 기준으로 그룹화하여 리스트에 저장
d2_list = [group for _, group in d2.groupby('대분류')]
# '지역분류' 그룹 추가
d2_list.append(d3)

# 3. 시각화 (파이차트)
for df in d2_list:
    # 시각화할 컬럼 선택 (메타데이터 컬럼 제외)
    cols_to_plot = [c for c in df.columns if c not in ['기간', '대분류', '분류']]
    
    # 데이터 정제: '-' 문자를 0.0으로 변환하고 실수형으로 변환
    df.loc[:, cols_to_plot] = df.loc[:, cols_to_plot].replace('-', 0.0)
    df.loc[:, cols_to_plot] = df.loc[:, cols_to_plot].astype(float)
    
    # 파이차트 그리기
    # subplots=True: 각 컬럼별로 별도의 파이차트 생성
    # layout: (행, 열) 배치 설정
    axes = df.loc[:, cols_to_plot].infer_objects(copy=False).plot(
        kind='pie',
        labels=df['분류'],
        subplots=True,
        figsize=(20, 5),
        layout=(1, len(cols_to_plot)),
        legend=False,
        autopct='%1.1f%%', # 퍼센트 표시 포맷
    )
    
    # 각 서브플롯 타이틀 설정 및 불필요한 라벨 제거
    for ax in axes.flatten():
        col_name = ax.get_ylabel()
        ax.set_title(col_name)
        ax.set_ylabel('') # y축 라벨(컬럼명) 제거 (타이틀로 옮김)
    
    # 레이아웃 조정 및 저장
    plt.gcf().tight_layout()
    
    # 대분류 이름으로 파일 저장 (예: 성별.png, 연령별.png ...)
    save_filename = df.iloc[0].loc['대분류'] + '.png'
    plt.savefig(save_filename)
    print(f"{save_filename} 저장 완료")

# plt.show() # 필요시 주석 해제하여 바로 확인 가능
