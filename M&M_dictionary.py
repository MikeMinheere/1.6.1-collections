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

mnmDictionaryBag = {
  'oranje' : str(kleurenPercentage[0]) + " oranje M&M's",
  'bruin' : str(kleurenPercentage[1]) + " bruine M&M's",
  'groen' : str(kleurenPercentage[2]) + " groene M&M's",
  'blauw' : str(kleurenPercentage[3]) + " blauwe M&M's"
}
print(list(mnmDictionaryBag.values()))