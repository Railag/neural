import os

from neural.config import Config


class Neuron:
    def __init__(self):
        self.w = [Config.get_random_w() for x in range(Config.k)]
        self.T = Config.start_T

    def sum(self, values):

        sum = 0
        i = 0

        for value in values:
            sum += value * self.w[i]
            i += 1

        result = sum - self.T

        print('neuron sum: ' + str(result))

        return result