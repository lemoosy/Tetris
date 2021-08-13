from const import *
import pygame, random


class Bloc:
    
    def __init__(self):
        
        self.matrix  =   BLOCS[random.randint(0, 6)]
        self.angle   =   random.randint(0, 3)
        self.color   =   random.randint(0, 4)

        self.__angle_def()
        
        self.x       =   random.randint(0, SIZE_MATRIX_X - len(self.matrix))
        self.y       =   4 - len(self.matrix)

        self.size_x  =   len(self.matrix[0])
        self.size_y  =   len(self.matrix)

    # TRANSFORMATIONS MATRICE

    def __transpose(self):

        self.matrix = list(map(list, zip(*self.matrix)))

    def __mirror_horizontal(self):

        self.matrix = [line[::-1] for line in self.matrix]

    def __mirror_vertical(self):
        
        self.__transpose()
        self.__mirror_horizontal()
        self.__transpose()
        
    # CONDITIONS
    
    def __out_of_dimension(self):

        if self.x < 0:
            return True

        if self.x + self.size_x == SIZE_MATRIX_X:
            return True

        if self.y + self.size_y == SIZE_MATRIX_Y:
            return True

        return False

    def collision(self, blocs):

        positions_bloc_1 = list()
        
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.matrix[y][x] == 1:
                    positions_bloc_1.append((x + self.x, y + self.y))

        for bloc in blocs:

            positions_bloc_2 = list()

            for y in range(bloc.size_y):
                for x in range(bloc.size_x):
                    if bloc.matrix[y][x] == 1:
                        positions_bloc_2.append((x + bloc.x, y + bloc.y))

            for position in positions_bloc_1:
                if position in positions_bloc_2:
                    return True

        return False

    # ANGLES
    
    def can_turn_left(self, blocs):

        self.turn_left()
        condition = not self.__out_of_dimension() and self.can_place(blocs)
        self.turn_right()

        return condition

    def can_turn_right(self, blocs):

        self.turn_right()
        condition = not self.__out_of_dimension() and self.can_place(blocs)
        self.turn_left()

        return condition

    def turn_left(self):

        self.angle = (self.angle + 1) % 4
        self.__angle_def()
            
    def turn_right(self):

        for i in range(3):
            self.angle = (self.angle + 1) % 4
            self.__angle_def()

    def __angle_def(self):

        if self.angle == 0:
            self.__angle_right()

        if self.angle == 1:
            self.__angle_up()

        if self.angle == 2:
            self.__angle_left()

        if self.angle == 3:
            self.__angle_down()

    def __angle_up(self):

        self.__transpose()

    def __angle_left(self):

        self.__transpose()
        self.__mirror_horizontal()
        self.__mirror_vertical()

    def __angle_down(self):

        self.__transpose()
        self.__mirror_horizontal()
        self.__mirror_vertical()

    def __angle_right(self):

        self.__transpose()

    # DÉPLACEMENTS

    def can_move_left(self, blocs):

        if self.x == 0:
            return False

        return True

    def can_move_down(self, blocs):

        if self.y + self.size_y == SIZE_MATRIX_Y:
            return False

        return True

    def can_move_right(self, blocs):

        if self.x + self.size_x == SIZE_MATRIX_X:
            return False

        return True

    def move_up(self):

        self.y -= 1

    def move_left(self):

        self.x -= 1

    def move_down(self):

        self.y += 1

    def move_right(self):

        self.x += 1

    # DESSINS

    def draw(self, window):

        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.matrix[y][x] != 0:
                    if y + self.y >= 3:
                        pygame.draw.rect(window, COLORS[self.color], pygame.Rect((self.x + x) * 100,  ((y + self.y) - 3) * 100, 100, 100))