from math import log, sqrt

from neural import Config


class NeuralMath:
    @staticmethod
    def update_V(V, alpha, y, t, yi):
        new_V = V - alpha * (y - t) * yi

        return new_V

    @staticmethod
    def update_T(T, alpha, y, t):
        new_T = T + alpha * (y - t)

        return new_T

    @staticmethod
    def update_W(W, y, t, yi, Vi, x, S):
        new_W = W - Config.alpha * (y - t) * yi * Vi * x * NeuralMath.calculate_yi_dash(S)

        return new_W

    @staticmethod
    def update_Tu(Tu, y, t, yi, Vi, S):
        new_Tu = Tu + Config.alpha * (y - t) * yi * Vi * NeuralMath.calculate_yi_dash(S)

        return new_Tu

    @staticmethod
    def calculate_yi_dash(S):
        yi_dash = 1 / sqrt(1 + S * S)

        return yi_dash

    @staticmethod
    def calculate_y(S):
        y = log(S + sqrt(S * S + 1))

        return y

    @staticmethod
    def calculate_E(y, t):
        s = 0
        i = 0
        for value in y:
            s += pow(value - t[i], 2)
            i += 1

        E = 0.5 * s

        return E
