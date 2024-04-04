import random
from attribute import Attribute
from character import Character
print("SELA BEM VINDO GUERREIRO, AO NOSSO PRIMEIRO JOGO DE RPG EM PYTHON ! É UMA HONRA RECEBER VOCÊ AQUI...VAMOS CRIAR UM PERSONAGEM?")
print("MAS FIQUE ATENTO ! ALGUNS PERSONAGENS PODEM RECEBER ALGO A MAIS DE ACORDO COM SUA CLASSE !")
print("NO MAIS, DIVIRTA-SE!")
attribute = Attribute()
name = input("OLÁ GUERREIRO, ESCOLHA O NOME DO SEU PERSONAGEM: ")
print("TEMOS ALGUMAS CLASSES DISPONIVEIS!")
print(" (1) dwarf(+2 em constituição)")
print(" (2) Elf(+2 em destreza)")
print(" (3) Human(+1 em todos os atributos)")
print(" (4) Barbaro(+2 em destreza)")
print(" (5) Dragonborn(+2 em força e +1 em carisma)")
print(" (6) Gnome(+2 em inteligencia)")
print(" (7) tieling(+1 em inteligencia e +2 em carisma)")
race = int(input("Digite o número da classe do seu persoagem: "))
sub_race = int
character = Character(name, race)
strength = random.randint(1,21)
dexterity = random.randint(1,21)
constitution = random.randint(1,21)
wisdom = random.randint(1,21)
intelligence = random.randint(1,21)
charisma = random.randint(1,21)
match race:
    case 1:
        constitution +=2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB RAÇA")
        print(" (1) Anão da Colina(+1 de sabedoria)")
        print(" (2) Anão da Montanha(+2 de força)")
        sub_race = input("OTIMO, AGORA DIGITE UM NUMERO PARA SUB RAÇA: ")
        if sub_race == 1:
            wisdom +=1
        else:
            strength+=2
    case 2:
        dexterity+=2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB RAÇA")
        print(" (1) Alto Elfo(+1 de inteligencia)")
        print(" (2) Elfo da floresta(+1 de sabedoria)")
        sub_race = input("OTIMO, AGORA DIGITE UM NUMERO PARA SUB RAÇA: ")
        if sub_race == 1:
            intelligence +=1
        else:
            wisdom+=1
    case 3:
        strength += 1 
        dexterity += 1
        constitution += 1
        wisdom += 1
        intelligence += 1
        charisma += 1    
    case 4:
        dexterity+=2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB RAÇA")
        print(" (1) Pés leves(+1 em carisma)")
        print(" (2) Parrudos(+1 em constituição)")
        sub_race = input("OTIMO, AGORA DIGITE UM NUMERO PARA SUB RAÇA: ")
        if sub_race == 1:
            charisma +=1
        else:
            constitution+=1
    case 5:
        strength +=2
        charisma +=1
    case 6:
        intelligence+=2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB RAÇA")
        print(" (1) Gnomo da Floresta(+1 em destreza)")
        print(" (2) Gnomo da Pedra(+1 em constituição)")
        sub_race = input("OTIMO, AGORA DIGITE UM NUMERO PARA SUB RAÇA: ")
        if sub_race == 1:
            dexterity +=1
        else:
            constitution+=1
    case 7:
        intelligence+=1
        charisma+=2        
print("ESTAS SÃO AS CARACTERISTICAS DO SEU PERSONAGEM")
print("Nome: ",character.definition_name(name))
match race:
    case 1:
        race = "dwarf"
        print("Classe: ",character.definition_race(race))
    case 2:
        race = "Elf"
        print("Classe: ",character.definition_race(race))
    case 3:
        race = "Human"
        print("Classe: ",character.definition_race(race))
    case 4:
        race = "Barbaro"
        print("Classe: ",character.definition_race(race))
    case 5:
        race = "Dragonborn"
        print("Classe: ",character.definition_race(race))
    case 6:
        race = "Gnome"
        print("Classe: ",character.definition_race(race))
    case 7:
        race = "tieling"
        print("Classe: ",character.definition_race(race))
if race == "dwarf" or race == "Elf" or race == "Barbaro" or race =="Gnome":
    print("Sub-Classe: ",character.definition_sub_race(sub_race))
print(attribute.definition_strength(strength))
print(attribute.definition_dexterity(dexterity))
print(attribute.definition_constitution(constitution))
print(attribute.definition_wisdom(wisdom))
print(attribute.definition_intelligence(intelligence))
print(attribute.definition_charisma(charisma))