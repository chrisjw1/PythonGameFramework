from Layers.Layer import Layer


class Screen(Layer):
    """Class which describes a screen the user can interact with. Only one screen exists at any time, and each
    screen is sandboxed from all others. It is the screen's responsibility to handle raw input and convert it into
     common sense events for the next layer down (or use it to create/destroy routines)"""
    def __init__(self,state):
        super().__init__()


    def transistion(self,next_screen=None):
        """Do all appropriate exit screen functions and move to next screen. If next_screen is None, exit the application"""
        self.onExit()
        # TODO logic for moving to next Screen
