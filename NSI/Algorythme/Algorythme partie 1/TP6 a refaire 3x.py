# Créé par damien.zuchetto, le 03/01/2023 en Python 3.7
#TP 6 3X
"""
def compteLettre(lettre,chaine):
    chaine="je vais au cine ce soir"
    lettre=0
    for b in range (len(chaine)):
        if lettre == "e":
            lettre+=1
print(compteLettre('e','je vais au cine ce soir'))


def compteLettre(lettre,chaine):
    compteur=0
    for n in range(0,len(chaine)):
        if chaine[n]==lettre:
            compteur+=1
    return compteur

print(compteLettre('e','je vais au cine ce soir'))

#ou

def compteLettre(lettre,chaine):
    compteur=0
    for c in chaine:
        if c==lettre:
            compteur+=1
    return compteur

print(compteLettre('e','je vais au cine ce soir'))

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
JourDepart=6
for k in range (1,32):
    print("{0:10}{1:2}decembre".format(semaine[JourDepart],k))
    JourDepart=(JourDepart+1)%7
"""

voyelles=['a','e','i','o','u','y']
Compteur=0
def compteVoyelles(chaine):
    if chaine==voyelles:
        compteur+=1
chaine=str(input("votre chaine ?"))
print(chaine,compteVoyelles(chaine))

