import pyglet
from Layers.Layer import Layer

class App(Layer):
    """Outermost layer of game. Manages the callbacks to they pyglet window"""
    def __init__(self,state_definition_path=None):
        super().__init__(state_definition_path)
        self.window = pyglet.window.Window()
        self.screen = None

        pass

    # TODO rename this to not be confused with onStart (or simply integrate it)
    def onStart(self):
        """Starts the application with the appropriate settings"""
        pyglet.app.run()
        pass
