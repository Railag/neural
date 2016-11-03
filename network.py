import os

from neural.neuron import Neuron
from neural.alphabet import Alphabet
from neural.result import Result
import PIL.Image, PIL.ImageTk


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

        result_string = ""
        for result_wrapper in result_wrappers:
            if result_wrapper.result:
                result_string += "\n Letter: " + result_wrapper.neuron.letter + " =" + str(result_wrapper.sum)

        print("results: " + result_string)

        return result_wrappers[0]

    def handle_file_line(self, filename):
        if not os.path.isfile(filename):
            return

        img, line_matrix, img_size = Network.prepare_line_image(filename)

        result_string = self.__recognize_line(line_matrix, img_size[0], img_size[1])

        return img, result_string

    @staticmethod
    def prepare_line_image(filename):
        try:
            img = PIL.Image.open(filename)
        except OSError as e:
            return

        rgb_im = img.convert('RGB')

        img_size = img.size

        img_width = img_size[0]
        img_height = img_size[1]

        size = img_width * 5, img_height * 5

        img = img.transform(size, PIL.Image.EXTENT, (0, 0, img_width, img_height))

        line_matrix = [[0 for x in range(img_width)] for y in range(img_height)]

        i = 0
        j = 0

        while i < img_height:
            while j < img_width:
                r, g, b = rgb_im.getpixel((j, i))
                white = r == 255
                if white:
                    line_matrix[i][j] = 0
                else:
                    line_matrix[i][j] = 1

                j += 1
            i += 1
            j = 0

        return img, line_matrix, img_size

    def __recognize_line(self, line_matrix, img_width, img_height):
        recognized_line = ""

        begin_x = 0
        end_x = 0

        letter_width = self.neurons[0].width
        letter_height = self.neurons[0].height

        while begin_x < img_width:

            begin_x = Network.find_begin_width(begin_x, line_matrix, img_width, img_height)

            if begin_x - end_x == Alphabet.space_width and end_x != 0:
                recognized_line += " "

            if begin_x != -1:

                end_x = begin_x + Alphabet.letter_width

                letter_matrix = [[0 for x in range(letter_width)] for y in range(letter_height)]

                k = begin_x
                index = 0

                while index < img_height:
                    width_index = 0

                    while k * (index + 1) < end_x * (index + 1):
                        letter_matrix[index][width_index] = line_matrix[index][k]

                        k += 1
                        width_index += 1

                    index += 1
                    k = begin_x

                letter_result = self.__analyze(letter_matrix)

                recognized_line += letter_result.neuron.letter

                begin_x = end_x

            else:
                return recognized_line

        return recognized_line

    @staticmethod
    def find_begin_width(i, line_matrix, img_width, img_height):
        begin_width = -1

        j = 0

        while i < img_width:
            while j < img_height:
                value = line_matrix[j][i]
                if value == 1:
                    begin_width = i
                    i = img_width
                    break

                j += 1
            i += 1
            j = 0

        return begin_width
