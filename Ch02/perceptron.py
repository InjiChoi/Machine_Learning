import numpy as np

# AND 게이트 구현
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0, 0)) # 0
print(AND(0, 1)) # 0
print(AND(1, 0)) # 0
print(AND(1, 1)) # 1


# 가중치와 편향 도입 
x = np.array([0, 1]) # 입력 => [0 1]
w = np.array([0.5, 0.5]) # 가중치 => [0.5 0.5]
b = -0.7 # 편향
w*x # array([0. , 0.5])
np.sum(w*x) # 0.5
np.sum(w*x) + b # -0.19999999999996 => 대략 -0.2 (부동소수점 수에 의한 연산 오차)


# 가중치와 편향을 도입한 AND 게이트 구현
def new_AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# NAND 게이트 구현 (AND와 가중치(w와 b)만 다름)
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# OR 게이트 구현 (AND와 가중치(w와 b)만 다름)
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# 단층 퍼셉트론으로는 XOR 게이트를 표현할 수 없음
# 단층 퍼셉트론으로는 비선형 영역을 분리할 수 없음
# 즉, 퍼셉트론을 조합해서(층을 쌓아서) XOR 게이트를 구현해야 함

# XOR 게이트 구현 (다층(2층) 퍼셉트론)
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0)) # 0
print(XOR(0, 1)) # 1
print(XOR(1, 0)) # 1
print(XOR(1, 1)) # 0

