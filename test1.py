import numpy as np

# a= 5


# z = np.clip(a, -100, None)
# print(z)


class LogisticNeuron:
    
    def __init__(self):
        self.w = None
        self.b = None

    def forpass(self, x):
        z = np.sum(x * self.w) + self.b  # 직선 방정식을 계산합니다
        return z
    def set_w(self, w):
        self.w = w   
    def set_b(self, b):
        self.b = b


# x = np.array([1,25,6,7,8])
# w = np.array([1,1,1,1,1])
# b = np.array([6, 3, 3 ,4 ,6])

# logi = LogisticNeuron()
# logi.set_b(b)
# logi.set_w(w)
# print(logi.forpass(x))

# print(np.sum(x*w))
# print(logi.)
n = 10

indexes = np.random.permutation(20)

# for i in indexes:
#     print(i)
print(indexes)