class Attribute:
    def __init__(self):
        self.__strength = int
        self.__dexterity = int
        self.__constitution = int
        self.__wisdom = int
        self.__intelligence = int
        self.__charisma = int

    @property
    def strength(self) -> int:
        return self.__strength
    
    @strength.setter
    def strenght(self, strength):
        self.__strength  = strength

    @property
    def dexterity(self) -> int:
        return self.__dexterity
    
    @dexterity.setter
    def dexterity(self,dexterity):
        self.__dexterity = dexterity

    @property
    def constitution(self) -> int:
        return self.__constitution
    
    @constitution.setter
    def constitution(self,constitution):
        self.__constitution = constitution

    @property
    def wisdom(self) -> int:
        return self.__wisdom
    
    @wisdom.setter
    def wisdom(self,wisdom):
        self.__wisdom = wisdom

    @property
    def intelligence(self) -> int:
        return self.__intelligence
    
    @intelligence.setter
    def intelligence(self,intelligence):
        self.__intelligence = intelligence

    @property
    def charisma(self) -> int:
        return self.__charisma
    
    @charisma.setter
    def charisma(self, charisma):
        self.__charisma = charisma

    def definition_strength(self,strength):
        self.__strength = strength
        
        if strength == 0:
            return f"Nível de Força igual a {strength}: Incorpório"
        elif strength >= 1 and strength <= 5 :
            return f"Nível de Força igual a {strength}: Incapaz"
        elif strength >=6 and strength <=9:
            return f"Nível de Força igual a {strength}: Fraco"
        elif strength >=10 and strength <=11:
            return f"Nível de Força igual a {strength}: Medino"
        elif strength >=12 and strength <=15:
            return f"Nível de Força igual a {strength}: Forte"
        elif strength >=16 and strength <=20:
            return f"Nível de Força igual a {strength}: Super poderoso"
        else:
            return f"Nível de Força igual a {strength}: Inbatível"

    def definition_dexterity(self, dexterity):
        self.__dexterity = dexterity
        
        if dexterity ==0:
            return f"Nível de Destreza igual a {dexterity}: Desacordado"
        elif dexterity >=1 and dexterity <=5:
            return f"Nível de Destreza igual a {dexterity}: Abatido"
        elif dexterity >=6 and dexterity <=9:
            return f"Nível de Destreza igual a {dexterity}: Desajeitado"
        elif dexterity >=10 and dexterity <=11:
            return f"Nível de Destreza igual a {dexterity}: Regular"
        elif dexterity >=12 and dexterity <=15:
            return f"Nível de Destreza igual a {dexterity}: Ágil"
        elif dexterity >=16 and dexterity <=20:
            return f"Nível de Destreza igual a {dexterity}: Ninja"
        else:
            return f"Nível de Destreza igual a {dexterity}: Inperceptível"
    
    def definition_constitution(self,constitution):
        self.__constitution = constitution
        
        if constitution ==0:
            return f"Nível de Costituição igual a {constitution}: Espectro"
        elif constitution >=1 and constitution <=5:
            return f"Nível de Costituição igual a {constitution}: Enfermo"
        elif constitution >=6 and constitution <=9:
            return f"Nível de Costituição igual a {constitution}: Frági"
        elif constitution >=10 and constitution <=11:
            return f"Nível de Costituição igual a {constitution}: Saudável"
        elif constitution >=12 and constitution <=15:
            return f"Nível de Costituição igual a {constitution}: Durão"
        elif constitution >=16 and constitution <=20:
            return f"Nível de Costituição igual a {constitution}: Super resistênte"
        else:
            return f"Nível de Costituição igual a {constitution}: Imortal"
    
    def definition_wisdom(self,wisdom):
        self.__wisdom = wisdom
    
        if wisdom ==0:
            return f"Nível de Sabedoria igual a {wisdom}: Inconscinte"
        elif wisdom >=1 and wisdom <=5:
            return f"Nível de Sabedoria igual a {wisdom}: Irracional"
        elif wisdom >=6 and wisdom <=9:
            return f"Nível de Sabedoria igual a {wisdom}: Desatento"
        elif wisdom >=10 and wisdom <=11:
            return f"Nível de Sabedoria igual a {wisdom}: Simples"
        elif wisdom >=12 and wisdom <=15:
            return f"Nível de Sabedoria igual a {wisdom}: Perspcaz"
        elif wisdom >=16 and wisdom <=20:
            return f"Nível de Sabedoria igual a {wisdom}: Filósofo"
        else:
            return f"Nível de Sabedoria igual a {wisdom}: Iluminado"

    def definition_intelligence(self,intelligence):
        self.__intelligence = intelligence
        
        if intelligence ==0:
            return f"Nível de Inteligencia igual a {intelligence}: Inanimado"
        elif intelligence >=1 and intelligence <=5:
            return f"Nível de Inteligencia igual a {intelligence}: Incivilizado"
        elif intelligence >=6 and intelligence <=9:
            return f"Nível de Inteligencia igual a {intelligence}: Parvo"
        elif intelligence >=10 and intelligence <=11:
            return f"Nível de Inteligencia igual a {intelligence}: Medíocre"
        elif intelligence >=12 and intelligence <=15:
            return f"Nível de Inteligencia igual a {intelligence}: Estuado"
        elif intelligence >=16 and intelligence <=20:
            return f"Nível de Inteligencia igual a {intelligence}: Gênio"
        else:
            return f"Nível de Intelicencia igual a {intelligence}: Onisciente"

    def definition_charisma(self,charisma):
        self.__charisma = charisma
        
        if charisma ==0:
            return f"Nível de Carisma igual a {charisma}: Aberração:"
        elif charisma >=1 and charisma <=5:
            return f"Nível de Carisma igual a {charisma}: Inexprecivo"
        elif charisma >=6 and charisma <=9:
            return f"Nível de Carisma igual a {charisma}: Rude"
        elif charisma >=10 and charisma <=11:
            return f"Nível de Carisma igual a {charisma}: Socíavel"
        elif charisma >=12 and charisma <=15:
            return f"Nível de Carisma igual a {charisma}: Persuasivo"
        elif charisma >=16 and charisma <=20:
            return f"Nível de Carisma igual a {charisma}: Influente"
        else:
            return f"Nível de Carisma igual a {charisma}: Ídolo"
           