class Screenshot:
    """A simple image taker"""
    def __init__(self,name):
        self._name=name

    def take(self):
        return "ClickPrtSc!"

class CreateGif:
    """A simple gif creator"""
    def __init__(self,name):
        self._name=name
    
    def take(self):
        return "Record!"

class ImageRight:
    """A simple law right"""
    def __init__(self,name):
        self._name=name

    def take(self):
        return "CopyrightInfrigment!"

# el factory esta fuera de las clases, no pertenece a nadie

def get_trickery(key='act1'):
    """This is the factory method"""
    actions=dict(act1=Screenshot('Class1'), act2=CreateGif('Class2'), act3=ImageRight('Class3'))
    return actions[key]

screen = get_trickery()
print(screen.take())

gif = get_trickery(key='act2')
print(gif.take())

right = get_trickery(key='act3')
print(right.take())



