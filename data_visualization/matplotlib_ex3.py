# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:41:55 2020

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

# matplotlib에서 사용할 폰트를 한글 폰트로 지정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

'''
# 산점도(scatter 그래프)
height = [165, 177, 160, 180, 185, 155, 172]
weight = [62, 67, 55, 74, 90, 43, 64]

size = 100 * np.arange(1, 8)  # 데이터별로 마커 크기 지정(값이 클수록 커짐)
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y']  # 데이터별로 마커 컬러 지정
plt.scatter(height, weight, s=size, c=colors, alpha=0.5)  # 그냥 c='b'로 컬러만 명시해도 ok
plt.xlabel('Height(m)')
plt.ylabel('Weight(Kg)')
plt.title('Height&Weight')
plt.grid(True)
'''

city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]  # 위도
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]  # 경도
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]  # 인구 밀도(2017)
size2 = np.array(pop_den) * 0.2
colors2 = ['r', 'g', 'b', 'c', 'm', 'k', 'y']

plt.scatter(lon, lat, s=size2, c=colors2, alpha=0.5)
plt.xlabel('경도(longitude)')
plt.ylabel('위도(latitude)')
plt.title('지역별 인구 밀도(2017)')

for x, y, name in zip(lon, lat, city):
    plt.text(x, y, name)  # 위도 경도에 맞게 도시 이름 출력

plt.show()
