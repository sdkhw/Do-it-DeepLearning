import numpy as np



# class LogisticNeuron:
    
#     def __init__(self):
#         self.w = None
#         self.b = None

#     def forpass(self, x):
#         z = np.sum(x * self.w) + self.b  # 직선 방정식을 계산합니다
#         return z
#     def backprop(self, x, err):
#         w_grad = x * err    # 가중치에 대한 그래디언트를 계산합니다
#         b_grad = 1 * err    # 절편에 대한 그래디언트를 계산합니다
#         return w_grad, b_grad
    
#     def activation(self, z):
#         z = np.clip(z, -100, None) # 안전한 np.exp() 계산을 위해
#         a = 1 / (1 + np.exp(-z))  # 시그모이드 계산
#         return a
        
#     def fit(self, x, y, epochs=1):
#         self.w = np.ones(x.shape[1])      # 가중치를 초기화합니다.
#         self.b = 0                        # 절편을 초기화합니다.
#         for i in range(epochs):           # epochs만큼 반복합니다
#             for x_i, y_i in zip(x, y):    # 모든 샘플에 대해 반복합니다
#                 z = self.forpass(x_i)     # 정방향 계산
#                 a = self.activation(z)    # 활성화 함수 적용
#                 err = -(y_i - a)          # 오차 계산
#                 w_grad, b_grad = self.backprop(x_i, err) # 역방향 계산
#                 self.w -= w_grad          # 가중치 업데이트
#                 self.b -= b_grad          # 절편 업데이트
#                 print("w", self.w)        # 절편 업데이트
#                 print("b", self.b)
#     def predict(self, x):
#         z = [self.forpass(x_i) for x_i in x]    # 정방향 계산
#         a = self.activation(np.array(z))        # 활성화 함수 적용
#         return a > 0.5


# x0 = [1.032e+01, 1.635e+01, 6.531e+01, 3.249e+02, 9.434e-02]

# x1 = [2.018e+01, 1.954e+01, 1.338e+02, 1.250e+03, 1.133e-01]

# x_val = []

# x_val.append(x0)
# x_val.append(x1)
# # x_val = np.append(x_val, x1, axis=0)
# x_val = np.array(x_val)
# print(x_val)

# y = np.array([0,1], dtype=np.int64)
# print(y)


# neuron = LogisticNeuron()
# neuron.fit(x_val, y)



l1 = [123, 244, 351, 114, 525]
w = [1,1,1,1,1]
b = 1

def activation(z):
    z = np.clip(z, -100, None) # 안전한 np.exp() 계산을 위해
    a = 1 / (1 + np.exp(-z))  # 시그모이드 계산
    return a

def predict(x):
    z = forpass(x)     # 정방향 계산
    return z > 0                   # 스텝 함수 적용


def forpass(x):
    z = np.dot(x, w) + b    # 직선 방정식을 계산합니다
    return z

forpass_result = forpass(l1)
activation_result = activation(forpass_result)

print(forpass_result)
print(activation_result)
prediction_result = predict(l1)
print(prediction_result)