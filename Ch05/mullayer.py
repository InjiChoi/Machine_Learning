# 곱셉 계층 구현
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y): # 순전파
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout): # 역전파
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

# 예시: 사과 쇼핑
apple = 100
apple_num = 2
tax = 1.1

# 계층들
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# 순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)
print(price) # 220

# 역전파
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
print(dapple, dapple_num, dtax) # 2.2 110 200