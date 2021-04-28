import numpy as np

x = np.random.rand(10, 1, 28, 28) # 무작위로 데이터 생성
print(x.shape) # (10, 1, 28, 28)
x[0].shape # (1, 28, 28)
x[1].shape # (1, 28, 28)

# 첫 번째 데이터의 첫 채널의 공간 데이터에 접근
x[0, 0]