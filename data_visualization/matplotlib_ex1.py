# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:23:16 2020

12. 데이터 시각화
"""

import matplotlib.pyplot as plt
import numpy as np

'''
# 선 그래프 예시
data1 = [10, 14, 19, 20, 25]
plt.plot(data1) #그래프_함수() 실행
plt.show() # 그래프 객체 정보 없이 그래프만 출력

# 2차원 선 그래프 예시
x = np.arange(-4.5, 5, 0.5)  # -4.5부터 5까지 0.5씩 증가하는 배열 생성
y = 2*x**2  # y=2x^2
[x, y]
plt.plot(x,y)
plt.show()

# 여러 데이터를 한 그래프 창에 한번에 표시하기
x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()

plt.figure()  # 새로운 그래프 창 생성
plt.plot(x, y2)  # 여기에 그래프 그림
plt.show()

plt.figure(3)  # 명시적으로 그래프 창 번호 지정 후 그림
'''
# %matplotlib qt : 그래프 창 명시적으로 보임 Figure 3
# %matplotlib inline : 그래프 창 번호 보이지 않음
'''
x2 = np.arange(-5, 5, 0.1)
y4 = x2**2 - 2
y5 = 20*np.cos(x2)**2  # NumPy에서 cos()는 np.cos()로 입력

plt.figure(1)
plt.plot(x2, y4)

plt.figure(2)
plt.plot(x2, y5)

plt.figure(1)
plt.plot(x2, y5)

plt.figure(2)
plt.clf()
plt.plot(x2, y4)

plt.show()
'''

# 그래프 영역 나누기 plt.subplot(m, n, p) #293p
x = np.arange(0, 10, 0.1)
y1 = 0.3*(x-5)**2 + 1
y2 = -1.5*x + 3
y3 = np.sin(x)**2  # NumPy에서 sin()는 np.sin()로 입력
y4 = 10*np.exp(-x) + 1  # NumPy에서 exp()는 np.exp()로 입력

# 2X2 행렬로 이뤄진 하위 그래프에서 p에 따라 위치 지정
plt.subplot(2, 2, 1)  # p는 1(좌상단)
plt.plot(x, y1)
plt.subplot(2, 2, 2)  # p는 2(우상단)
plt.plot(x, y2)
plt.subplot(2, 2, 3)  # p는 3(죄하단)
plt.plot(x, y3)
plt.subplot(2, 2, 4)  # p는 4(우하단)
plt.plot(x, y4)
plt.show()

plt.plot(x, y1, x, y2)


# 그래프 출력범위 지정
x = np.linspace(-4, 4, 100)  # [-4, 4] 범위에서 100개의 값 생성
y1 = x**3
y2 = 10*x**2 - 2

plt.plot(x, y1, x, y2)
plt.show()

# 그래프 출력범위 지정, 관심영역 확대
plt.plot(x, y1, x, y2)
plt.xlim(-1, 1)  # x축은 -1~1까지만 출력
plt.ylim(-3, 3)  # y축은 -3~3까지만 출력
plt.show()