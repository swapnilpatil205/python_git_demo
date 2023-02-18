class animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

    @property
    def get_animal_name(self):
        print("This is {0}, and has {1} legs".format(self.name,self.legs))