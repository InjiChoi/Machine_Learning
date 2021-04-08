import numpy as np

# way 1 (실수(부동소수점)만 인수로 가능)
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# way 2 (넘파이 배열도 지원)
def step_function2(x):  # x = [-1.0, 1.0, 2.0]
    y = x > 0   # y = array([False, True, True], dtype=bool)
    return y.astype(np.int) # y = array([0, 1, 1])


y1 = step_function(1.0)
y2 = step_function(0)
y3 = step_function(2.0)

print(y1)
print(y2)
print(y3)

x = np.array([1.0, 0, 2.0])
y = step_function2(x)
print(y)
