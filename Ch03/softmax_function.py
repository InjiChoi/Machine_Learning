import numpy as np

# 항등 함수
def identity_function(x):
    return x

# 소프트맥스 함수
def softmax(a):
	exp_a = np.exp(a)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y


# overflow example
a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a))) # 제대로 계산되지 않음 => [nan nan nan]
c = np.max(a) # c = 1010 (최댓값)
print(a - c) # [  0 -10 -20]
# 입력 신호 중 최댓값(c)를 빼주면 올바르게 계산할 수 있다.
print(np.exp(a - c) / np.sum(np.exp(a - c))) # [9.99954600e-01 4.53978686e-05 2.06106005e-09]

# 개선 후 소프트맥스 함수
def fixed_softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y