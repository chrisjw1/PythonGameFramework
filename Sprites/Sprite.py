import yaml

def Sprite(object):
    def __init__(self,layout_file:str):
        parsed_layout = yaml.load(layout_file)
        
