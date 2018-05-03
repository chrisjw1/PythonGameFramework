import yaml

class Layer(object):

    def __init__(self,state_definition_path:str=None):
        if state_definition_path:
            self.state = yaml.load(open(state_definition_path))
        else:
            self.state = {}
        self.child_layers = []

    def update(self,delta_time):
        self.onUpdate(delta_time)
        for child_layer in self.child_layers:
            child_layer.update(delta_time)

    def onUpdate(self,delta_time):
        pass

    def start(self):
        """Screen has just started and all application settings have been cleared"""
        self.onStart()

    def onStart(self):
        pass

    def onPause(self):
        pass

    def pause(self):
        """Logic to do before focus is lost (eg minimized)"""
        self.onPause()

    def exit(self):
        self.onExit()
        for child_layer in child_layers:
            child_layer.exit()

    def onExit(self):
        pass

    def onDraw(self):
        pass

    def draw(self):
        self.onDraw()
        for child_layer in child_layers:
            child_layer.draw()

a = yaml.load(open('sampleState.yaml'))
pass
