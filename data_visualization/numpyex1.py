# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:42:40 2020

"""

import numpy as np
data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1) #Numpy 배열 생성
a1

data2 = [0.1, 5, 4, 12, 0.2]
a2 = np.array(data2) #Numpy 실수배열 생성(이 경우 정수도 실수로 표현)
a2

np.array([0.5, 2, 0.1, 8]) #리스트 데이터 직접 넣어 객체 생성
np.array([1,2,3], [4,5,6], [7,8,9]) #다차원 배열 객체 생성

arr_obj = np.arange(0, 10, 2)
print(arr_obj) # [0 2 4 6 8]

b1 = np.arange(12).reshape(4,3) #일차원배열을 4X3 행렬로 변경(세로4)
b1.shape #만들어진 배열의 형태 보는 법 (4,3)이면 4X3
arr_obj.shape #(5,)면 요소 5개인 일차원배열

np.linspace(1, 10, 20) #1부터 10까지 20개의 데이터 생성
np.linspace(0, np.pi, 20) #0부터 파이까지 20개의 데이터 생성

# 11장 훑어보았는데 그때그때 찾아보는 게 더 나을 것 같아 넘어감 