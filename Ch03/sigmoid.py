import numpy as np
import matplotlib.pyplot as plt


# 시그모이드 함수
# 넘파이의 브로드캐스트 기능 덕분에 인수로 배열도 가능
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))   # 결과: [0.26894142 0.73105858 0.88079708]

# 그래프로 그려보기
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()