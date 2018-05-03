from Layers.Layer_2_Screen import Screen

class CBScreen(Screen):
    def __init__(self):
        super().__init__()
        self.child_layers.append[CBActivity()]
