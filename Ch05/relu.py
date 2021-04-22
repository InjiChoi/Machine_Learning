import numpy as np

class Relu:
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

x = np.array([[1.0, -0.5], [-2.0, 3.0]])
print(x)

mask = (x <= 0)
print(mask) # [[False True] [True False]]

### "mask"는 True/False로 구성된 넘파이 배열
### 순전파의 입력인 x의 원소 값이 0 이하인 인덱스는 True, 
### 그 외(0보다 큰 원소)는 False로 유지