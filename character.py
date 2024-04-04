class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.__sub_race = int

    @property
    def sub_race(self) -> int:
        return self.__sub_race
    
    @sub_race.setter
    def strenght(self, sub_race):
        self.__sub_race  = sub_race

    def definition_name(self, name_character):
        self.name = name_character
        return name_character 
    
    def definition_race(self, race_character):
        self.race = race_character 
        return race_character
    
    def definition_sub_race(self,sub_race_character):
        self.__sub_race = sub_race_character
        return sub_race_character