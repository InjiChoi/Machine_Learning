import numpy as np

# ReLU : Rectified Linear Unit
# 입력이 0을 넘으면 그 입력을 그대로 출력
# 0 이하이면 0을 출력

def relu(x):
    return np.maximum(0, x)