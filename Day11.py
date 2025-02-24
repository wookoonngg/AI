import numpy as np
import pandas as pd

# a=np.array([1,3.5,7])
# print (a,a.ndim)
#
# b = np.array([[]])


ones = np.ones((3,4))
print (ones)
zeros = np.zeros((3,4))
zeros = np.zeros((3,4), dtype=np.int16)
print(zeros)

# a = np.arrage(5, 11)
# print(a, a.ndim, a.shape, a.size)

a = np.arrange(5, 11,2)
print(a, a.ndim, a.shape, a.size)

df = pd.DataFrame(

    data {"a" : [4,5,6],
          "b" : [7,8,9],
          "c" : [10,11,12]}, index = [1,2,3]


)