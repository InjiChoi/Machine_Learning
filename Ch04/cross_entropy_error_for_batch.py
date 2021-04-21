import numpy as np

# y: 신경망의 출력
# t: 정답 레이블

def cross_entropy_error_1(y, t):
    if y.ndim == 1: # y가 1차원이라면(데이터 하나당 교차 엔트로피를 구하는 경우)
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y+1e-7)) / batch_size
 
### 정답 레이블이 원-핫 인코딩이 아니라 숫자 레이블로 주어졌을 때
def cross_entropy_error_2(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
