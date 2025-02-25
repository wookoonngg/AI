# Assignment1 - 결축치 값을 산술평균으로 채워 넣는 다양한 방법을 적용하시오.
# Assignment 2 - 위 과제의 사이킬러 라이브러리를 주석처리 하고 결축치를 산술평균으로 채워 넣으시오

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
        'A' : [1,2, np.nan,4],
        'B' : [np.nan, 12,3,4],
        'C' : [1,2,3,4]
    }
)

print(df)

df.fillna(df.mean(), inplace = True)

print ("평균으로 채운 뒤 데이터\n" , df)