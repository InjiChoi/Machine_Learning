def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_2(x):
    return x[0]**2 + x[1]**2 # 또는 np.sum(x**2)

# x0=3, x1=4일 때, x0에 대한 편미분
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0
print(numerical_diff(function_tmp1, 3.0)) # 6.00000000000378

# x0=3, x1=4일 때, x1에 대한 편미분
def function_tmp2(x1):
    return 3.0*2.0 + x1*x1
print(numerical_diff(function_tmp2, 4.0)) # 7.999999999999119