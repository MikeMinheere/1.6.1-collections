import random

def ZakMenems(kleuren):
    aantalVanKleur = [0,0,0,0]
    aantalMenems = int(input("hoeveel M&M's wil je in de zak? "))
    zak = list()
    for x in range (0,aantalMenems):
        randomChoice = random.randint(0, 3)
        aantalVanKleur[int(randomChoice)] += 1
        zak.append(kleuren[randomChoice]) 
    return zak,aantalVanKleur 
kleurenPercentage = [0,0,0,0]
zak = list()
kleuren = ['oranje', 'bruin', 'groen', 'blauw']
zak, kleurenPercentage= ZakMenems(kleuren)
print(str(kleurenPercentage[0]) + " oranje M&M's")
print(str(kleurenPercentage[1]) + " bruine M&M's")
print(str(kleurenPercentage[2]) + " groene M&M's")
print(str(kleurenPercentage[3]) + " blauwe M&M's")

