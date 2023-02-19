from datetime import date
class animal:
    def __init__(self,name,legs,birth_year):
        self.name = name
        self.legs = legs
        self.birth_year = birth_year

    @property
    def get_animal_name(self):
        print("This is {0}, and has {1} legs".format(self.name,self.legs))

    @property
    def get_age(self):
        todays_date = date.today()
        print("{0} is {1} years of age".format(self.name,(todays_date.year-self.birth_year)))

        