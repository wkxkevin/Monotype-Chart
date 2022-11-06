import math
import re
import sys
import time

def print_dex():
    for x in dex:
       print(x)

types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
types_short = ['No', 'Fi', 'Wa', 'El', 'Gr', 'Ic', 'Fi', 'Po', 'Gr', 'Fl', 'Ps', 'Bu', 'Ro', 'Gh', 'Dr', 'Da', 'St', 'Fa']
spec = ["Calyrex", "Necrozma", "Urshifu", "Arceus", "Silvally", "Wormadam", "Hoopa", "Rotom", "Shaymin", "Oricorio"]
alola = ["Rattata", "Raticate", "Raichu", "Sandshrew", "Sandslash", "Vulpix", "Ninetales", "Diglett", "Dugtrio", "Meowth", "Persian", "Geodude", "Graveler", "Golem", "Grimer 	", "Muk", "Exeggutor", "Marowak"]
galar = ["Meowth", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Farfetch'd", "Weezing", "Mr. Mime", "Articuno", "Zapdos", "Moltres", "Slowking", "Corsola", "Zigzagoon", "Linoone", "Darumaka", "Darmanitan", "Darmanitan", "Yamask", "Stunfisk"]

# Get every pokemon and their type
dex = {}
with open("Dex.txt", "r") as f:
    for l in f:
        line = l.strip().split("\t")
        dex[line[0]] = [line[1]]
        if(len(line) == 3):
            dex[line[0]].append(line[2])

#get each pokemon and determine type
def get_teams(file):
    txt_f = open(file, "r")
    txt_f.readline()
    txt_f.readline()

    p1 = txt_f.readline()
    p2 = txt_f.readline()
    p1team = p1[p1.find("team\":")+7:p1.find("rating")-3].split("]")
    p2team = p2[p2.find("team\":")+7:p2.find("rating")-3].split("]")
    p1 = []
    p2 = []
    for i in p1team:
        p1.append(re.split("\|", i)[0:3])
    for i in p2team:
        p2.append(re.split("\|", i)[0:3])
    return p1,p2

def get_winner(file):
    html_f = open(file, "r").read()
    lines = html_f.split("\n")
    names = [lines[16].split("|")[3], lines[17].split("|")[3]]
    idx = html_f.index("|win|")
    winner = html_f[idx+5:html_f.index("\n", idx)]
    if(winner == names[0]):
        return 0
    elif(winner == names[1]):
        return 1
    else :
        return -1

def get_type(player):
    types = {}
    for pokemon in player:
        pkmn = pokemon[0]
        if(pokemon[1] == None and (pokemon[0] in spec or pokemon[0] in spec or pokemon[0] in alola)):
            pkmn = pokemon[1]
        elif(pkmn == "Zacian" and pkmn[2] == RustedSword):
            pkmn = pokemon[1]
        elif(pkmn == "Zamazenta" and pkmn[2] == RustedShield):
            pkmn = pokemon[1]
        for i in dex[pkmn]:
            if(i in types):
                types[i] += 1
            else:
                types[i] = 1

    for i in dict(sorted(types.items(), key=lambda item: item[1], reverse = True)):
        return i

sys.stdout = open("output.txt", "w")
#Test for one battle
start = time.time()
p1,p2 = get_teams("test.txt")
print(get_winner("test.html"))
print(get_type(p1))
print(get_type(p2))
print("--- %s seconds ---" % (time.time() - start))
print(p1)
print(p2)

#get monotype chart(input_log, battle_log, and directory are temporary)
mu_chart = [[0]*18]*18
for input_log, battle_log in firectory:
    p1,p2 = get_teams(input_log)
    winner = get_winner(battle_log)
    type1 = get_type(p1)
    type2 = get_type(p2)
    if(winner == 0):
        mu_chart[types[type1]][types[type2]] += 1
    elif(winner == 0):
        mu_chart[types[type2]][types[type1]] += 1
