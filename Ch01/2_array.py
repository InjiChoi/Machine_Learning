import numpy as np

### 1.5.2 넘파이 배열 생성하기
x1 = np.array([1.0, 2.0, 3.0])
print(x1)
print(type(x1)) # <class 'numpy.ndarray'>


### 1.5.3 넘파이의 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(x + y) # 원소별 덧셈 => [3. 6. 9.]
print(x * y) # 원소별 곱셈 => [2. 8. 18.]
print(x / y) # 원소별 나눗셈 => [0.5 0.5 0.5]
print(x / 2.0) # 브로드캐스트(스칼라값과의 계산이 넘파이 배열의 원소별로 한 번씩 수행) => [0.5 1. 1.5]

### 1.5.4 넘파이의 N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape) # 2 X 2 행렬 => (2, 2)
print(A.dtype) # 행렬에 담긴 원소의 자료형 => int32
print(A * 10) # 브로드캐스트 기능 작동 => [[10 20] [30 40]]

B = np.array([[3, 0], [0, 6]])
print(A * B) # 원소별 곱셈 => [[3 0] [0 24]]

### 1.5.5 브로드캐스트
A = np.array([[1, 2], [3, 4]])
B = np.array([[10, 20]])
print(A * B) # B가 2차원 배열(행렬)로 변형된 후 원소별 연산이 이루어짐 => [[10 40] [30 80]]

### 1.5.6 원소 접근
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X.shape) # (3, 2) 3행 2열
print(X[0]) # 0행 => [51 55]
print(X[0][1]) # (0, 1) 원소 => 55

for row in X:
    print(row)
X = X.flatten() # 1차원 배열로 변환
print(X) # [51 55 14 19 0 4]
print(X[np.array([0, 2, 4])]) # index가 0, 2, 4인 원소 추출 => [51 14 0]
