import bloc, copy, threading, time
from main import can_place_bloc, collision


class MyThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        self.bloc = None

    def run(self):

        while True:

            time.sleep(1)

            copy_bloc = copy.deepcopy(self.bloc)
            copy_bloc.move_down()
            if can_place_bloc()
            


            self.bloc.move_down()
            
            if self.bloc.X + (len(self.bloc) - 1) > 12:
                return
            
            