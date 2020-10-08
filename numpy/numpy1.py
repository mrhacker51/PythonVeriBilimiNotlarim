#!/usr/bin/python3

import numpy as np

# Normal
my_list = list(range(21))

print(my_list)

result = np.array(my_list)

print(result,"\n",type(result))

print("-"*30)

## Matrix 
matrixlistesi = [[10,20,30],[40,50,60],[70,80,90]]

print(matrixlistesi)

result = np.array(matrixlistesi)

print(result)

print(result[0],"\n",result[1],"\n",result[2])

# Veri analizi yaparken daha güzel görüntü saglar matrix görünüm çok önemlidir.
