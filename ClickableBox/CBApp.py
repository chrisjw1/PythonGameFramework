from Layers.Layer_1_App import App
from ClickableBox.CBScreen import CBScreen

class CBApp(App):
    def __init__(self):
        super().__init__()
        self.child_layers.append(CBScreen)
