import random

import numpy
from mako.template import Template
from weasyprint import HTML, CSS

from classes.WordExtractor import WordExtractor


class BingoCard:

    def __init__(self):
        self._11 = ""
        self._12 = ""
        self._13 = ""
        self._14 = ""
        self._21 = ""
        self._22 = ""
        self._23 = ""
        self._24 = ""
        self._31 = ""
        self._32 = ""
        self._33 = ""
        self._34 = ""
        self._41 = ""
        self._42 = ""
        self._43 = ""
        self._44 = ""

    def create_randomized_win(self, filepath):
        word_extractor = WordExtractor()
        numbers = range(8, 12)
        content_word_number = random.choice(numbers)
        word_number = 16 - content_word_number

        words = word_extractor.get_n_words(word_number)
        content_words = word_extractor.get_n_content_words(content_word_number)

        matrix = self.get_empty_matrix()
        position = range(4)

        winning_words = content_words.copy()
        while len(content_words) > 0:
            x = random.choice(position)
            y = random.choice(position)
            word = random.choice(content_words)
            if matrix[x][y] == "":
                matrix[x][y] = str(word)
                content_words.remove(word)
                if len(content_words) < 1:
                    winning_chances = False
                    diagonal_counter = 0
                    for i in range(4):
                        y_counter = 0
                        x_counter = 0
                        for j in range(4):
                            if matrix[i][j] != "":
                                x_counter += 1
                            if i == j and matrix[i][j] != "":
                                diagonal_counter += 1
                            if matrix[j][i] != "":
                                y_counter += 1
                        if x_counter == 4 or y_counter == 4 or diagonal_counter == 4:
                            print("x - {} , y- {}, dia - {}".format(x_counter, y_counter, diagonal_counter))
                            winning_chances = True
                    if winning_chances is False:
                        content_words = winning_words
                        matrix = self.get_empty_matrix()
        while len(words) > 0:
            x = random.choice(position)
            y = random.choice(position)
            l_word = words[0]
            if matrix[x][y] == "":
                matrix[x][y] = str(l_word)
                words.remove(l_word)
        self.matrix_to_object(matrix)
        self.to_pdf(filepath)

    def create_randomized_loss(self, filepath):
        word_extractor = WordExtractor()
        numbers = range(3, 6)
        content_word_number = random.choice(numbers)
        word_number = 16 - content_word_number

        words = word_extractor.get_n_words(word_number)
        content_words = word_extractor.get_n_content_words(content_word_number)

        matrix = numpy.empty([4, 4], dtype="<U30")

        for i in range(4):
            for j in range(4):
                matrix[i][j] = ""
        position = range(4)
        winning_words = content_words
        while len(content_words) > 0:
            x = random.choice(position)
            y = random.choice(position)
            word = random.choice(content_words)
            diagonal_counter = 0
            y_counter = 0
            x_counter = 0
            if matrix[x][y] == "":
                if x == y:
                    for i in range(4):
                        if matrix[i][i] in winning_words:
                            diagonal_counter += 1
                for i in range(4):
                    if matrix[x][i] in winning_words:
                        x_counter += 1
                    if matrix[i][y] in winning_words:
                        y_counter += 1
                if y_counter < 3 and x_counter < 3 and diagonal_counter < 3:
                    matrix[x][y] = str(word)
                    content_words.remove(word)
        while len(words) > 0:
            x = random.choice(position)
            y = random.choice(position)
            l_word = words[0]
            if matrix[x][y] == "":
                matrix[x][y] = str(l_word)
                words.remove(l_word)
        self.matrix_to_object(matrix)
        self.to_pdf(filepath)


    def matrix_to_object(self, matrix):
        self._11 = matrix[0][0]
        self._12 = matrix[0][1]
        self._13 = matrix[0][2]
        self._14 = matrix[0][3]
        self._21 = matrix[1][0]
        self._22 = matrix[1][1]
        self._23 = matrix[1][2]
        self._24 = matrix[1][3]
        self._31 = matrix[2][0]
        self._32 = matrix[2][1]
        self._33 = matrix[2][2]
        self._34 = matrix[2][3]
        self._41 = matrix[3][0]
        self._42 = matrix[3][1]
        self._43 = matrix[3][2]
        self._44 = matrix[3][3]

    def to_pdf(self, filepath):
        mytemplate = Template(filename='/home/kevin/PycharmProjects/BingoCardCreator/src/html/bingo-template.html')
        str = mytemplate.render(
            aa=self._11,
            ab=self._12,
            ac=self._13,
            ad=self._14,
            ba=self._21,
            bb=self._22,
            bc=self._23,
            bd=self._24,
            ca=self._31,
            cb=self._32,
            cc=self._33,
            cd=self._34,
            da=self._41,
            db=self._42,
            dc=self._43,
            dd=self._44
        )
        html = HTML(string=str)
        css = CSS(string=
                  'div { background: #ffffff; width: 140px; height: 140px; border: solid black; display: inline-block; }.square h1 {color: #000000; text-align: center;} span {word-wrap: normal;}')
        html.write_pdf(
            filepath, stylesheets=[css])

    @staticmethod
    def get_empty_matrix():
        matrix = numpy.empty([4, 4], dtype="<U30")

        for i in range(4):
            for j in range(4):
                matrix[i][j] = ""
        return matrix
