from basic import *
from const import *
import copy, pygame


class Matrix:

    class __Size(Vector):

        pass

    def __init__(self, x, y):

        self.__matrix = [[0 for x in range(x)] for y in range(y)]
        self.size = self.__Size(x, y)

    def value(self, x, y):

        return self.__matrix[y][x]

    def reset_line(self, y):

        for x in range(self.size.x):
            self.__matrix[y][x] = 0

    def edit_line(self, y, new_line):

        for x in range(self.size.x):
            self.__matrix[y][x] = copy.deepcopy(new_line[x])

    def can_break_lines(self):

        loop = True
        lines = list()

        for y in range(self.size.y):

            if self.__matrix[y][0] == 0:
                continue

            for value in self.__matrix[y]:
                if self.__matrix[y][0] != value:
                    loop = False

            if loop:
                lines.append(y)
            
        return lines

    def break_lines(self, lines):

        for line in lines:
            for y in range(line, 0, -1):
                self.edit_line(y, self.__matrix[y - 1])

        self.reset_line(0)

    def draw(self, window, shape):

        matrix_copy = copy.deepcopy(self.__matrix)
        self.set_shape(shape)
        window.fill((0,0,0))

        for y in range(SIZE_MATRIX_Y):
            for x in range(SIZE_MATRIX_X):
                if self.__matrix[y][x] != 0:
                    pygame.draw.rect(window, COLORS[self.__matrix[y][x] - 1], pygame.Rect(x * SIZE_BLOC_X,  y * SIZE_BLOC_Y, SIZE_BLOC_X, SIZE_BLOC_Y))

        pygame.display.flip()
        self.__matrix = copy.deepcopy(matrix_copy)

    def set_shape(self, shape):

        for y in range(shape.size.y):
            for x in range(shape.size.x):
                if shape.value(x, y) != 0:
                    if y + shape.position.y >= 0:
                        self.__matrix[y + shape.position.y][x + shape.position.x] = COLORS.index(shape.color) + 1