# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:55:47 2020

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

# 그래프 꾸미기: fmt 옵션 이용

x = np.arange(0, 5, 1)  # 배열 범위 [0, 5], 1씩 증가
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()

# fmt 옵션: 선 컬러 지정
plt.plot(x, y1, 'm', x, y2, 'y', x, y3, 'k', x, y4, 'c')  # 아래에서부터 1234
plt.show()

# fmt 옵션: 선 스타일 지정
plt.plot(x, y1, '-', x, y2, '--', x, y3, ':', x, y4, '-.')  # 아래에서부터 1234
plt.show()

# fmt 옵션: 마커로 표시
plt.plot(x, y1, 'o', x, y2, '^', x, y3, 's', x, y4, 'd')  # 아래에서부터 1234
plt.show()

# 폰트 변경(한글 출력 가능하도록)
font_list = matplotlib.font_manager.get_fontconfig_fonts()
font_names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in font_list]

# 사용 가능한 폰트 이름을 생성하는 코드(파일생성o, 동작확인x)
f = open("D:\myPyCode\my_font_list.txt", 'w')
for font_name in font_names:
    f.write(font_name + "\n")
f.close()

# matplotlib에서 사용할 폰트를 한글 폰트로 지정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# fmt 옵션: 선 컬러, 스타일, 마커 다양하게 지정
# 표 라벨, 제목, 격자, 문자열 표시
plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')  # 아래에서부터 1234
plt.legend(['data1', 'data2', 'data3', 'data4'], loc = 'best')  # 범례 표시
plt.xlabel('X축')  # X축에 라벨 추가 axis-중심선
plt.ylabel('Y축')
plt.title('Graph title')  # 상단 중심에 그래프 타이틀 추가
plt.grid(True)  # 격차 추가
plt.text(2.5, 1, "문자열 출력 가능")
plt.show()

