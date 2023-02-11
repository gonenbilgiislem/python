# -*- coding: utf-8 -*-

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])
print(sayilar[::-1])

#print(sayilar[6])
#print(sayilar[0:3])

sayilar2 = np.array([[0,5,10],[15,20,25]])
print(sayilar2[:,0:2])

print(sayilar2[-1,:])
print(sayilar2[:,-1])

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)