import yaml

class Layer(object):

    def __init__(self,state_definition_path:str=None):
        if state_definition_path:
            self.state = yaml.load(open(state_definition_path))
        else:
            self.state = {}
        self.child_layers = []

a = yaml.load(open('sampleState.yaml'))
pass