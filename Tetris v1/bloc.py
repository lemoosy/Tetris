from const import *
import random


class Bloc:
    
    def __init__(self):
        
        self.bloc    =   BLOCS[random.randint(0, 6)]
        self.angle   =   random.randint(0, 3)
        self.color   =   random.randint(0, 4)
        self.x       =   random.randint(0, SIZE_MATRIX_X - len(bloc))
        self.y       =   2

        self.__init_angle()

    def __transpose(self):

        self.matrix = list(map(list, zip(*self.matrix)))

    def __mirror_horizontal(self):

        self.matrix = [line[::-1] for line in self.matrix]

    def __mirror_vertical(self):
        
        self.__transpose()
        self.__mirror_horizontal()
        self.__transpose()
        
    def __init_angle(self):

        # UP
        if self.angle == 1:
            self.__transpose()
            self.__mirror_horizontal()
            self.__mirror_vertical()

        # LEFT
        if self.angle == 2:
            self.__mirror_horizontal()
            self.__mirror_vertical()

        # DOWN
        if self.angle == 3:
            self.__transpose()

    def can_place(self, blocs):

        for bloc in blocs:

            if collision(self.bloc, bloc):
                return False

            return True

    def draw(self):

        pass


def collision(bloc_1, bloc_2):

    positions_bloc_1 = list()
    positions_bloc_2 = list()

    for y in range(len(bloc_1.matrix)):
        for x in range(len(bloc_1.matrix[0])):

            if bloc_1.matrix[y][x] == 1:
                positions_bloc_1.append((bloc_1.X + x, bloc_1.Y + y))

            if bloc_2.matrix[y][x] == 1:
                positions_bloc_2.append((bloc_2.X + x, bloc_2.Y + y))

    for position in positions_bloc_1:
        if position in positions_bloc_2:
            return True

    return False