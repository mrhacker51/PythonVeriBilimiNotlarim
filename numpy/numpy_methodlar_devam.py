#!/usr/bin/python3

import numpy as np

# random.randn

result = np.random.randn(10)

"""
Output : 

[-0.01040726  0.66458531 -1.01757481  1.80514712 -0.25749435  0.13783834
 -0.33127386 -0.62654978 -0.07408637  0.24677015]

"""

result = np.random.randn(1,10)

"""
Output : 


[[-1.95042202 -1.52976763 -0.13186076  0.4872268   0.9010817  -0.19689923
  -1.60622371  0.27387558  0.88594755  0.35713576]]


"""


# random.randint

result = np.random.randint(4)

"""
Output :  3
"""

result = np.random.randint(1,20,2)

"""
Output : 

[11  3]

"""
print(result)
