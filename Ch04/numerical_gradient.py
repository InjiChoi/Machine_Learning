import numpy as np
from partial_derivative import function_2

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
    
    return grad

# (3, 4)에서의 기울기 => 결과: [6. 8.]
print(numerical_gradient(function_2, np.array([3.0, 4.0])))
# (0, 2)에서의 기울기 => 결과: [0. 4.]
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
# (3, 0)에서의 기울기 => 결과: [6. 0.]
print(numerical_gradient(function_2, np.array([3.0, 0.0])))