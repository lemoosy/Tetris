from bloc import *
from const import *
import copy, pygame, time


def draw_blocs(window, bloc):

    window.fill((0,0,0))

    bloc.draw(window)

    for bloc in blocs:
        bloc.draw(window)

    pygame.display.flip()


pygame.init()
window = pygame.display.set_mode((1000, 1000))
blocs = list()
TIMES = [1000]
DIFFICULTY = 1
pygame.time.Clock()


while True:

    bloc = Bloc()
    draw_blocs(window, bloc)

    if bloc.collision(blocs):
        break

    loop = True

    while loop:

        if TIMES[len(TIMES) - 1] <= pygame.time.get_ticks():

            TIMES.append(TIMES[len(TIMES) - 1] + 700 - (DIFFICULTY * 100))

            if bloc.can_move_down(blocs):
                copy_bloc = copy.deepcopy(bloc)
                copy_bloc.move_down()
                if not copy_bloc.collision(blocs):
                    bloc.move_down()
                    draw_blocs(window, bloc)
                else:
                    loop = False
                    break
            else:
                loop = False
                break
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if bloc.can_turn_left(blocs):
                        bloc.turn_left()
                        draw_blocs(window, bloc)

                if event.key == pygame.K_LEFT:
                    if bloc.can_move_left(blocs):
                        copy_bloc = copy.deepcopy(bloc)
                        copy_bloc.move_left()
                        if not copy_bloc.collision(blocs):
                            bloc.move_left()
                            draw_blocs(window, bloc)

                if event.key == pygame.K_DOWN:
                    if bloc.can_turn_right(blocs):
                        bloc.turn_right()
                        draw_blocs(window, bloc)

                if event.key == pygame.K_RIGHT:
                    if bloc.can_move_right(blocs):
                        copy_bloc = copy.deepcopy(bloc)
                        copy_bloc.move_right()
                        if not copy_bloc.collision(blocs):
                            bloc.move_right()
                            draw_blocs(window, bloc)

    blocs.append(bloc)

print("Game Over !")