import os
import random

from neural.neural_math import NeuralMath
from neural.neuron import Neuron
from neural.config import Config

curr_value = 0


class Network:
    def __init__(self):
        self.neurons = []
        self.V = []
        self.T = Config.start_T

        for i in range(0, Config.neurons_count):
            self.neurons.append(Neuron())
            self.V.append(random.uniform(Config.min_w, Config.max_w))

    def teach(self, all_values):
        global curr_value

        E = 1
        y = 0

        ys = []
        expected_values = []

        while E > Config.Em and y == 0:

            while curr_value < len(all_values):

                values = Network.get_next_values(curr_value, all_values)
                expected_value = Network.get_next_predict(all_values)

                sums = []
                for neuron in self.neurons:
                    sums.append(neuron.sum(values))

                S = self.inner_sum(sums)
                y = NeuralMath.calculate_y(S)
                print(y)

                ys.append(y)
                expected_values.append(expected_value)


            E = NeuralMath.calculate_E(ys, expected_values)

            if E < Config.Em:
                return y
            else:
                curr_value = 0
                E = 0
                y = 0
                self.update_weights(ys, expected_values, sums, all_values)

    def update_weights(self, y, t, yi, values):
        for i in range(0, Config.neurons_count):
            self.V[i] = NeuralMath.update_V(self.V[i], Config.alpha, y, t, yi[i])

        self.T = NeuralMath.update_T(self.T, Config.alpha, y, t)

        j = 0
        for neuron in self.neurons:
            for i in range(0, Config.k):
                neuron.w[i] = NeuralMath.update_W(neuron.w[i], y, t, yi[i], self.V[i], values[i], yi[i])

            neuron.T = NeuralMath.update_Tu(neuron.T, y, t, yi[j], self.V[j], yi[j])
            j += 1

    def inner_sum(self, values):

        sum = 0
        i = 0

        for value in values:
            sum += value * self.V[i]
            i += 1

        result = sum - self.T

        return result

    @staticmethod
    def get_next_predict(y):
        global curr_value
        if len(y) > curr_value:
            return y[curr_value + Config.k - 1]
        else:
            return -1

    @staticmethod
    def get_next_values(i, y):
        global curr_value
        if len(y) > i + Config.k:
            curr_value += 1
            return y[i:i + Config.k]
        else:
            return y[i:len(y)]
