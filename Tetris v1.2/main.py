from const import *
from matrix import Matrix
from shape import Shape
import copy, pygame


pygame.init()
window = pygame.display.set_mode((SIZE_MATRIX_X * SIZE_BLOC_X, SIZE_MATRIX_Y * SIZE_BLOC_Y))
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Tetris v1.2 - Game by Léonard Lemoosy")
matrix = Matrix(SIZE_MATRIX_X, SIZE_MATRIX_Y)
pygame.time.Clock()
TIMES = [1000 - 100 * LEVEL]


while True:

    shape = Shape()
    matrix.draw(window, shape)
    loop = True

    while loop:

        if TIMES[len(TIMES) - 1] <= pygame.time.get_ticks():

            FUTUR_TIME = TIMES[len(TIMES) - 1] + (1000 - 100 * LEVEL)
            TIMES.append(FUTUR_TIME)

            if shape.can_move_down(matrix):
                shape.move_down()
                matrix.draw(window, shape)
            else:
                loop = False
                break

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if shape.can_turn_left(matrix):
                        shape.turn_left()
                        matrix.draw(window, shape)

                if event.key == pygame.K_LEFT:
                    if shape.can_move_left(matrix):
                        shape.move_left()
                        matrix.draw(window, shape)

                if event.key == pygame.K_DOWN:
                    if shape.can_turn_right(matrix):
                        shape.turn_right()
                        matrix.draw(window, shape)

                if event.key == pygame.K_RIGHT:
                    if shape.can_move_right(matrix):
                        shape.move_right()
                        matrix.draw(window, shape)

    matrix.set_shape(shape)

    lines = matrix.can_break_lines()
    matrix.break_lines(lines)
    LEVEL += len(lines)

    if shape.position.y < 0:
        break

print("Game Over !")