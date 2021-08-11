from bloc import Bloc
from thread import MyThread
import pygame


blocs = list()
falling_bloc = MyThread()


while True:

    bloc = Bloc()
    
    if not bloc.can_place(blocs):
        break

    falling_bloc.bloc = bloc
    falling_bloc.start()
    GAME = True
    
    while GAME:

        for event in pygame.event.get():

            if not bloc.can_place(blocs):
                GAME = False
                break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    pass

                elif event.key == pygame.K_LEFT:
                    pass

                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_RIGHT:
                    pass

    blocs.append(bloc)


print("Game Over !")