from Layers.Layer import Layer

class Entity(Layer):
    def __init__(self,state_definition_path=None):
        super().__init__(state_definition_path)
