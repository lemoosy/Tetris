from const import *
import pygame, random


class Shape:
    
    def __init__(self):
        
        self.shape          =       SHAPES[random.randint(0, len(SHAPES) - 1)]
        self.color          =       COLORS[random.randint(0, len(COLORS) - 1)]
        self.size           =       None
        self.angle          =       random.randint(1, 4)

        for i in range(self.angle):
            self.turn_left()

        self.position       =       self.__Position(random.randint(0, SIZE_MATRIX_X - self.size.x), -self.size.y)

    class __Position:

        def __init__(self, x, y):

            self.x = x
            self.y = y

    class __Size(__Position):

        pass

    # TRANSFORMATIONS MATRICE

    def __transpose(self):

        self.shape = list(map(list, zip(*self.shape)))

    def __mirror_horizontal(self):

        self.shape = [line[::-1] for line in self.shape]

    def __mirror_vertical(self):
        
        self.__transpose()
        self.__mirror_horizontal()
        self.__transpose()
        
    # CONDITIONS
    
    def __out_of_dimension(self):

        if self.position.x == -1:
            return True

        if self.position.x + (self.size.x - 1) == SIZE_MATRIX_X:
            return True

        if self.position.y + (self.size.y - 1) == SIZE_MATRIX_Y:
            return True

        return False

    def collision(self, matrix):

        for y in range(self.size.y):
            for x in range(self.size.x):
                if self.shape[y][x] == 1:
                    if y + self.position.y >= 0:
                        if matrix[y + self.position.y][x + self.position.x] != 0:
                            return True

        return False

    # ANGLES

    def can_turn_left(self, matrix):

        self.turn_left()
        condition = not self.__out_of_dimension() and not self.collision(matrix)
        self.turn_right()

        return condition

    def can_turn_right(self, matrix):

        self.turn_right()
        condition = not self.__out_of_dimension() and not self.collision(matrix)
        self.turn_left()

        return condition

    def turn_left(self):

        self.__transpose()
        self.__mirror_vertical()
        self.size = self.__Size(len(self.shape[0]), len(self.shape))

    def turn_right(self):

        for i in range(3):
            self.turn_left()

    # DÉPLACEMENTS

    def can_move_left(self, matrix):

        self.move_left()
        condition = not self.__out_of_dimension() and not self.collision(matrix)
        self.move_right()

        return condition

    def can_move_down(self, matrix):

        self.move_down()
        condition = not self.__out_of_dimension() and not self.collision(matrix)
        self.move_up()

        return condition

    def can_move_right(self, matrix):

        self.move_right()
        condition = not self.__out_of_dimension() and not self.collision(matrix)
        self.move_left()

        return condition

    def move_up(self):

        self.position.y -= 1

    def move_left(self):

        self.position.x -= 1

    def move_down(self):

        self.position.y += 1

    def move_right(self):

        self.position.x += 1