import numpy as np

# 나쁜 구현 예
def numerical_diff_1(f, x):
    h = 10e-50 # h에 작은 값 대입
    return (f(x+h) - f(x)) / h

### 문제1: 반올림 오차 문제 발생 => 개선점: 10^-4를 h로 사용
### 문제2: f의 차분 문제 발생 => 개선점: 중심 차분(중앙 차분) 계산

# 두 개선점 적용한 수치 미분 구현
def numerical_diff_2(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)