from Layers.Layer import Layer

class Activity(Layer):
    """Class describes an activity for the user, like playing the game or
    navigating the pause menu"""
    def __init__(self,state_definition_path=None):
        super().__init__(state_definition_path)
        
