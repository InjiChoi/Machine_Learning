import numpy as np
from numerical_gradient import numerical_gradient

# f: 최적화하려는 함수 
# init_x: 초기값
# lr: learning rate(학습률)
# step_num: 경사법에 따른 반복 횟수
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

### Q1. 경사법으로 f2의 최솟값을 구하라
def function_2(x):
    return np.sum(x**2)

init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)) 
# [-6.11110793e-10  8.14814391e-10]

### 학습률이 너무 큰 예 : lr = 10.0
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100)) 
# 큰 값으로 발산 => [-2.58983747e+13 -1.29524862e+12]

### 학습률이 너무 작은 예 : lr = 1e-10
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100)) 
# 거의 갱신되지 않은 채 끝 => [-2.99999994  3.99999992]
