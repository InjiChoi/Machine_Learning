import numpy as np

# 1차원 배열
A = np.array([1, 2, 3, 4])
print(A) # [1 2 3 4]
print(np.ndim(A)) # 배열의 차원 수 => 1 
print(A.shape) # (4,) : 튜플로 반환
print(A.shape[0]) # 4

# 2차원 배열(행렬)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B) # [[1 2] br [3 4] br [5 6]]
print(np.ndim(B)) # 2
print(B.shape) # (3, 2) : 3X2 배열 (3행 2열)

# 행렬의 곱셈(1)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B)) # [[19 22] br [43 50]]

# 행렬의 곱셈(2) - 행렬의 형상에 주의하기
# 다차원 배열을 곱하려면 두 행렬의 대응하는 차원의 원소 수를 일치시켜야 함
A = np.array([[1, 2, 3], [4, 5, 6]]) # 2X3
B = np.array([[1, 2], [3, 4], [5, 6]]) # 3X2
print(np.dot(A, B)) # [[22 28] br [49 64]]

# 행렬의 곱셈(3)
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])
# B1 = np.array([[7], [8]])
print(B.shape) # (2,)
# print(B1.shape) # (2, 1)
print(np.dot(A, B)) # [23 53 83]
print(np.dot(A, B).shape) # (3, )

# 신경망에서의 행렬 곱
X = np.array([1, 2])
X.shape # (2, )
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W) # [[1 3 5] br [2 4 6]]
W.shape # (2, 3)
Y = np.dot(X, W)
print(Y) # [5 11 17]