# 📚 Python 데이터 분석 스터디 (Python Data Analysis Study)

## 📖 프로젝트 개요 (Overview)
이 저장소는 Python을 활용한 데이터 분석 역량을 기르기 위한 학습 공간입니다.
- **Python 기본 문법**부터 **Pandas**를 활용한 심화 데이터 처리까지 다룹니다.
- 실제 데이터를 활용한 **EDA(탐색적 데이터 분석)** 및 **미니 프로젝트**를 진행합니다.
- 학습한 내용을 정리하고(`study/`), 코드로 실습하며(`practice/`), 결과물을 리포트(`report/`)로 남깁니다.

## 📂 디렉토리 구조 (Directory Structure)
```
study_python/
├─ study/                   # 📘 학습 문서 (이론 및 정리)
│   ├─ 02. python_pandas.md                # Pandas 기초
│   ├─ 02_1. python_pandas_advanced.md    # Pandas 심화 (Groupby, Pivot 등)
│   └─ ...
├─ practice/                # 💻 실습 노트북 (Jupyter Notebook)
│   ├─ practicetitanic.ipynb               # 타이타닉 데이터 실습
│   ├─ practicepandaspivot.ipynb           # 피벗 테이블 실습
│   └─ ...
├─ report/                  # 📊 분석 리포트 & 미니 프로젝트
│   └─ datapractice2/
│       └─ datapracticechicken.ipynb       # 서울시 일반음식점 분석
├─ data/                    # 💾 데이터셋 (CSV, Excel 등)
└─ README.md                # 📍 이 파일 (프로젝트 메인)
```

## 🗓️ 6주 완성 학습 플랜 (Learning Plan)
| 주차 | 주제 | 핵심 내용 | 관련 실습/문서 |
|:---:|:---|:---|:---|
| **1주차** | **Python 기초** | 변수, 자료형, 제어문, 함수 | `practicepandas1.ipynb` |
| **2주차** | **Numpy & Pandas 입문** | 배열(Array), Series, DataFrame 생성 | `practicetitanic.ipynb` |
| **3주차** | **데이터 선택 & 조작** | 인덱싱, 슬라이싱, `loc`/`iloc`, 데이터 삭제 | `02. python_pandas.md` |
| **4주차** | **그룹 분석 심화** | `groupby`, `agg`, `transform`, `apply` | `02_1. python_pandas_advanced.md` |
| **5주차** | **데이터 재구조화** | `pivot_table`, `crosstab`, `melt` | `practicepandaspivot.ipynb` |
| **6주차** | **실전 프로젝트** | 데이터 로드부터 시각화까지 전 과정 (서울시 맛집) | `datapracticechicken.ipynb` |

## 🚀 사용 방법 (How to Use)
1. **학습하기**: `study/` 폴더의 마크다운 문서를 읽으며 개념을 익힙니다.
2. **실습하기**: `practice/` 폴더의 노트북을 열어 예제 코드를 직접 실행해 봅니다.
3. **적용하기**: `data/` 폴더의 데이터를 활용해 나만의 분석을 시도해 봅니다.
4. **기록하기**: 배운 내용이나 분석 결과를 새로운 노트북으로 저장하고 커밋합니다.

---
> **Tip**: 학습 중 궁금한 점이나 에러(`UnicodeDecodeError` 등)는 해결 과정을 주석이나 마크다운으로 기록해 두면 큰 자산이 됩니다. 화이팅! 🎉
