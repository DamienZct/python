# Créé par Damien.zuchetto, le 02/02/2023 en Python 3.7
"""
stock={'poires':5,'pommes':10,'fraises':35}
print(len(stock))
print(stock['fraises'])


stock={'poires':5,'pommes':10,'fraises':35}
inventaire=""
for nom in stock.keys():
    inventaire += nom + ', '
print(inventaire)

stock={'poires':5,'pommes':10,'fraises':35}
for num in stock.values():
    print (num)

stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

for nom, num in stock.items():
    print(nom, '->',num)


stock = {'poires': 5, 'pommes': 10, 'fraises': 35}



print('fraises' in stock.keys())
print('banane' in stock.keys())
print(7 in stock.values())
print(5 in stock.values())
print(3 in stock.values())

stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
stock["fraises"]=20
print(stock)
stock["abricots"]=15
print(stock)

stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
del stock["fraises"]
print(stock)
valeur = stock.pop("pommes")
print(stock)
print(valeur)


d = { 'nom':'Dupuis' , 'prenom':'Jacques', 'age':30}
for nom in d.keys():
    inventaire+= nom + ','
for num in d.values():
    print(inventaire,num)


print("jaques dupuis a 30 ans")


courses = {'Croissant':6 , 'Pizza': 2, 'Café en grains (sachet de 500gr)':3,'riz(sachet de 1 kilogramme)':1}
print(courses)

courses = {'Croissant':6 , 'Pizza': 3, 'Café en grains (sachet de 500gr)':3,'riz(sachet de 1 kilogramme)':1}
print(courses)

def occurrences(chaine):
   D = {}
   for caractere in chaine:
      if caracetre in D.keys():
          D[caractere]=D[Caractere]+1
      else:
          D[caractere] = 1
   return D

print(occurrences('tortue'))

def anagramme(chaine1, chaine2):
   occurrenceChaine1 = occurrences(chaine1)
   occurrenceChaine2 = occurrences(chaine2)
   del occurenceChaine1[' ']
   del occurenceChaine2[' ']
   return occurenceChaine1 == occurenceChaine2

def renduMonnaie(somme, pieces):
	choisies={}
	for p in pieces:
		choisies[p]= 0
		while somme>= p:
			somme=somme-p
			choisies[p]+=1
		return choisies
pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pèces choisies sont')
print(renduMonnaie(somme,pieces))


import csv
fichier = open("ballon2019.csv","r",encoding="utf-8")
lecture_fichier=csv.dictReader(fichier, delimiter=',')
liste_enregistrement=[]
for ligne in lecture_fichier:
    liste_enregistrement.append(dict(ligne))
fichier.close()

for enregistrement in list enregistrement :
    print(enregistrement [‘durée’], enregistrement[‘altitude m’]
"""
from pylab import *

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
plot(x, y) # affiche y en fonction de x

show() # affiche la figure l’écran

