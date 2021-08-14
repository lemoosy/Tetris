from shape import *
from const import *
import copy, pygame, time


def past_shape_on_matrix(shape, matrix):

    for y in range(shape.size.y):
        for x in range(shape.size.x):

            if shape.shape[y][x] == 0:
                continue

            if y + shape.position.y < 0:
                continue

            if y + shape.position.y >= SIZE_BLOC_Y:
                continue

            if x + shape.position.x >= SIZE_BLOC_X:
                continue

            matrix[y + shape.position.y][x + shape.position.x] = COLORS.index(shape.color) + 1

    return matrix

def draw_shape_and_matrix(shape):

    window.fill((0,0,0))

    matrix_copy = copy.deepcopy(matrix)
    matrix_copy = past_shape_on_matrix(shape, matrix_copy)

    for y in range(SIZE_MATRIX_Y):
        for x in range(SIZE_MATRIX_X):
            if matrix_copy[y][x] != 0:
                pygame.draw.rect(window, COLORS[matrix_copy[y][x] - 1], pygame.Rect(x * SIZE_BLOC_X,  y * SIZE_BLOC_Y, SIZE_BLOC_X, SIZE_BLOC_Y))

    pygame.display.flip()

def break_line():

    for line in matrix:

        if line[0] == 0:
            return

        old_value = line[0]

        for value in line:

            if value != old_value:
                return


pygame.init()
window = pygame.display.set_mode((SIZE_MATRIX_X * SIZE_BLOC_X, SIZE_MATRIX_Y * SIZE_BLOC_Y))
matrix = [[0 for x in range(SIZE_MATRIX_X)] for y in range(SIZE_MATRIX_Y)]
TIMES = [1000]
pygame.time.Clock()


while True:

    shape = Shape()
    draw_shape_and_matrix(shape)

    if shape.collision(matrix):
        print('looooool')
        break

    loop = True

    while loop:

        if TIMES[len(TIMES) - 1] <= pygame.time.get_ticks():

            TIMES.append(TIMES[len(TIMES) - 1] + 300 - (LEVEL * 100))

            if shape.can_move_down(matrix):
                shape.move_down()
                draw_shape_and_matrix(shape)
            else:
                loop = False
                break
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if shape.can_turn_left(matrix):
                        shape.turn_left()
                        draw_shape_and_matrix(shape)

                if event.key == pygame.K_LEFT:
                    if shape.can_move_left(matrix):
                        shape.move_left()
                        draw_shape_and_matrix(shape)

                if event.key == pygame.K_DOWN:
                    if shape.can_turn_right(matrix):
                        shape.turn_right()
                        draw_shape_and_matrix(shape)

                if event.key == pygame.K_RIGHT:
                    if shape.can_move_right(matrix):
                        shape.move_right()
                        draw_shape_and_matrix(shape)

    matrix = past_shape_on_matrix(shape, matrix)

    if shape.position.y < 0:
        break

print("Game Over !")