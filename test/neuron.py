import os

import PIL.Image, PIL.ImageTk


class Neuron:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0 for x in range(width)] for y in range(height)]

    def setup_w0(self, w0):
        self.w0 = w0

    def teach(self, callback):
        again = False
        i = 0
        while i < 12:
            result, valid = self.teach_file("C:\\Users/Railag/Downloads/bpp/true/image" + str(i) + ".bmp", True,
                                            callback)  # valid
            if result != valid:  # false for valid image
                again = True
            result2, valid = self.teach_file("C:\\Users/Railag/Downloads/bpp/false/n" + str(i) + ".bmp", False,
                                             callback)  # invalid
            if result2 != valid:  # true for invalid image
                again = True

            i += 1

        if again:
            self.teach(callback)

    def update_weights(self, tmp_matrix, plus):
        i = 0
        j = 0

        while i < self.height:
            while j < self.width:
                value = tmp_matrix[i][j]
                self.handle_pixel(i, j, value, plus)

                j += 1
            i += 1
            j = 0

    def handle_pixel(self, j, i, param, valid):
        if param == 1:
            if valid:
                self.matrix[j][i] += 1
            else:
                self.matrix[j][i] -= 1

    def get_matrix(self):
        i = 0
        j = 0
        line = ""

        line += '\n'

        while i < self.height:
            while j < self.width:
                line += str(self.matrix[i][j]) + " "
                j += 1
            line += '\n'
            i += 1
            j = 0

        return line

    def process_image(self, filename, w0, teach, valid):
        try:
            img = PIL.Image.open(filename)
        except OSError as e:
            return

        rgb_im = img.convert('RGB')

        size = 125, 200

        img = img.transform(size, PIL.Image.EXTENT, (0, 0, 5, 8))

        tmp_matrix = [[0 for x in range(w0)] for y in range(self.height)]

        i = 0
        j = 0

        while i < self.height:
            while j < self.width:
                r, g, b = rgb_im.getpixel((j, i))
                white = r == 255
                if white:
                    tmp_matrix[i][j] = 0
                else:
                    tmp_matrix[i][j] = 1

                j += 1
            i += 1
            j = 0

        sum = 0
        i = 0
        j = 0

        while i < self.height:
            while j < self.width:
                value = tmp_matrix[i][j]

                sum += value * self.matrix[i][j]

                j += 1
            i += 1
            j = 0

        print(sum)
        result = sum > w0

        if teach and result != valid:
            if not result and valid:
                self.update_weights(tmp_matrix, True)
            elif result and not valid:
                self.update_weights(tmp_matrix, False)

        return result, sum, img

    def handle_file(self, filename):

        if not os.path.isfile(filename):
            return

        result, sum, img = self.process_image(filename, self.w0, False, False)

        return result, sum, img

    def teach_file(self, filename, valid, callback):

        if not os.path.isfile(filename):
            return False, False

        result, sum, img = self.process_image(filename, self.w0, True, valid)

        callback()

        return result, valid
