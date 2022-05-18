## 1. 모델이 어떻게 동작하는가
- 머신러닝은 "과거"의 특정한 "패턴"을 통해 목적에 대해 "예측"하는 것이다.

### Decision Tree
- 더 성능 좋은 모델이 있지만, 이해하기 쉽고 데이터 사이언스의 기초를 하기 아주 적합한 모델이다.
- 두개의 분기로 나뉘는 조건을 만들고 학습을 진행함

## 2. 기본적인 데이터 탐색
- 어떤 프로젝트도 가장 처음 해야할 일은 데이터를 가공하여 친숙하게(familiarize) 해야한다.
- pandas: 데이터를 탐색 및 조작하는 데이터 사이언스 도구
  ```python
  import pandas as pd
  ```
    - dataframe: pandas의 가장 중요한부분으로, 테이블 형태의 데이터이다.

```python
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()
```

