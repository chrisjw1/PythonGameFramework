import pyglet
from Layers.Layer import Layer

class App(Layer):
    """Outermost layer of game. If this were a framework I would have my implementation """
    def __init__(self):
        super().__init__('AppModelDefinition.yaml')
        self.window = pyglet.window.Window()
        self.screen = None
        pass

    def start(self):
        """Starts the application with the appropriate settings"""
        pyglet.app.run()
        pass


app = App()
app.start()