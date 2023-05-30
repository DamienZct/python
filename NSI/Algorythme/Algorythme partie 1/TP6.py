#chaine de caractère - TP6
"""
phrase = "bonjour"
print (phrase[1:4])

chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)


w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))

chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')

chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')

s = "Welcome"
print(s[-1])
print(s[-2])

s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])

s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))

chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)

ch = 'A'
print(ord(ch))

valeur=66
print(chr(valeur))

chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)

def compteLettre(lettre,chaine):
    print(chaine.count(lettre))
    return compteLettre
print(compteLettre('e','je vais au cine ce soir'))


def compteLettre(lettre,chaine):
    chaine="je vais au cine ce soir"
    lettre=0
    for b in range (len(chaine)):
        if lettre == "e":
            lettre+=1
print(compteLettre('e','je vais au cine ce soir'))


def fonctionpremierMot(chaine):
    pos=chaine.find(" ") #5
    return chaine[:pos]
print(fonctionpremierMot("enfin il arrête de pleuvoir "))

print("Un peu")
print("Beaucoup")
print("Passionnément")

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in range(len(semaine)):
    print (semaine[i])



semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in semaine:
    print (i)



semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for jour in semaine:
    print(jour)

depart=3-1
for n in range(1,32):
    print(semaine[(n+depart)%7],n,"decembre")


#Exercice 7
voyelles=['a','e','i','o','u','y']
def compteVoyelles(chaine):
    somme=0
    for v in voyelles:
        somme = somme + chaine.count(v)
    return somme
chaine=str(input("votre chaine ?"))
print(chaine,compteVoyelles(chaine))


#Exercice 8
def compteDesMots(chaine):
    chaine.count(" ")
    return chaine.count(" ")
chaine=str(input("votre chaine ?"))
print(chaine,compteDesMots(chaine))



#Exercice 9
#lycée Touchard
latitude="47° 59.698'N"
longitude="  0° 12.276'E"

#VLT au Chili
#latitude="24° 37.649'S"
#longitude=" 70° 24.250'W"


#Exercice 10
valeur=int(input("saisir un nombre entre 1 et 12"))

compteur=0
for rouge in range(1,7):
    for vert in range(1,7):
        somme= rouge+vert
        if somme == valeur:
            compteur+=1
print("ilya", compteur, "facons de faire", valeur,"avec deux dés.")


#Compliment
#Ex1
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=' ' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))



#Exercice 2
cr="*"
def insertionTexte(texte):
    ntexte=texte[0]
    for i in texte:
        ntexte=ntexte+cr+i

    return ntexte

chaine="touchard"
print(insertionTexte(chaine)[2:])

#Exercice 2 correction
def inversionMot(texte):
    nouveautexte=''
    for indice in range(len(texte)-1):
        nouveautexte+=texte[indice]+"*"
    return nouveautexte
texte=str(input('votre texte?'))
print (inversionMot(texte))

#Exercice 3:
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]

print(chaine,total)

#Exercie4:
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]

print(chaine,total)
if chaine==total:
    print("good")

#Exercice 5:
def codecesar(phrase,cle):
    total=''
    for i in range(0,len(phrase)):
        ascii=ord(phrase[i])
        conv=ascii-65+cle
        caract=chr(conv+65)
        total+=caract+""
    return total

cle=int(input("clef"))
phrase=str(input("phrase"))
print(codecesar(phrase,cle))
"""

#Exercice6:
from string import ascii_uppercas as ascUp
vignereTable = [ascUp[i:]+ascUp[i:] for i in range(len(ascUp))]
for ligne in range(0,len(vignereTable)):
    print(ligne, vignereTable[ligne])

def vigenere(vignereTable,mot,cle):
    lettrecle=0
    for i in cle:
        lettrecle.append(i)
    print(lettrecle)




mot='misericorde'


