import os

from neural.neuron import Neuron
from neural.alphabet import Alphabet
from neural.result import Result


class Network:
    def __init__(self, width, height):
        self.neurons = []
        for char in Alphabet.letters:
            self.neurons.append(Neuron(width, height, char))

    def setup_w0(self, w0):
        for neuron in self.neurons:
            neuron.setup_w0(w0)

    def teach(self, callback):
        for neuron in self.neurons:
            neuron.teach(callback)

    def handle_file(self, filename):

        if not os.path.isfile(filename):
            return

        img, tmp_matrix = Neuron.prepare_image(self.neurons[0], filename)

        result = self.__analyze(tmp_matrix)

        return img, result

    def __analyze(self, tmp_matrix):
        result_wrappers = []

        for neuron in self.neurons:
            result, sum = neuron.check_image(tmp_matrix)
            result_wrappers.append(Result(neuron, result, sum))

        result_wrappers.sort(key=lambda x: x.sum, reverse=True)

        return result_wrappers[0]
