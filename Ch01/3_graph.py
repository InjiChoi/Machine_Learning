import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

### 1.6.1 단순한 그래프 그리기
# 데이터 준비
# np.arange(start ,end, interval)
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()

### 1.6.2 pyplot의 기능
# 데이터 준비
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend() # 범례 (Legend)는 그래프에 데이터의 종류를 표시하기 위한 텍스트
plt.show()

### 1.6.3 이미지 표시하기
img = imread('sample.png') # 이미지 읽어오기
plt.imshow(img)
plt.show()