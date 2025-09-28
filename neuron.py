class Neuron:

    def __init__(self):
        self.w = 1.0
        self.b = 1.0

    def forpass(self, x):
        y_hat = x * self.w + self.b # 직선의 방정식 계산
        return y_hat

    def backpropagation(self, x, err):
        w_grad = x * err
        b_grad = 1 * err
        return w_grad, b_grad
    

    def fit(self, x, y, epochs = 4000):

        for i in range(epochs):
            for x_i, y_i in zip(x,y):
                y_hat = self.forpass(x_i)
                err = -(y_i - y_hat)

                w_grad , b_grad = self.backpropagation(x_i, err) # 역방향 계산
                self.b -= b_grad
                self.w -= w_grad
