"""
a=4
b=3.2
c="hello"
print (a,b,c,"->",end="") #pas de retour àla ligne
print (a+5) #affichage de variable avec retour à la ligne
print("bonjoure") #affichage de texte avec retour àla ligne

-------------------------------------------------------------------


a=19
if a>10:
    print("ok")
print("test")

a=10
if a>10:
    print("ok")
print("test")

a=9
if a>10:
    print("ok")
print("test")

-------------------------------------------------------------------

a=int(input("veuillez entrez un nombre svp"))
a=a+5
print(a)


a = 5
b = 6
if a == 2 or b == 3:
    print("ok")
else:
    print("non")


a=34
b=6
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a%b
i=b**2
print(c,d,e,f,g,h,i)

for k in range (0,5):
    print(k,end="")

for k in range (0,11,2):
    print(k,end="")

for k in range (6,-1,-1):
    print(k,end="")

k=0
while k<18:
    print(k,end="")
    k=k+1

n=6
while n>=-5:
    print(n,end="")
    n=n-1                    #commentaire


a = int(input("votre valeur de debut"))
print(a)
b = int(input("votre valeur de fin"))
print(b)
for n in range (a, b+1):
    print(n)


a= int(input("votre valeur de départ"))
print(a)
for n in range (1,10+1):
    print(n)

a= int(input("votre table de multiplication"))
print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)


valeur=0
somme=0
while valeur >= 0:
    valeur = int(input("écrivez un nombre svp "))
    somme = valeur+somme
print("la somme des nombres est ", somme )



menu='0'
while menu != 'q':
       print("1=charger le fichier ")
       print("2= sauvegarder le fichier ")
       print("3= afficher les donnée ")
       print("4= modifier les données ")
       print("q=quitter")
       menu=input("Votre choix ? ")
       if menu == '1':
             print(" chargement ")
       elif menu == '2':
             print(" sauvegarde ")
       elif menu == '3':
             print(" Affichage ")
       elif menu == '4':
             print(" modification ")
       elif menu == 'q':
             print(" au revoir ")
       else:
          print(" erreur ")


from random import *
nombre = randint(1,20)
valeur=0
while valeur != nombre:
      print("votre chiffre")
      valeur=int(input("choisi un chiffre"))
      if valeur>nombre:
         print("chiffre trop grand")
      elif valeur<nombre:
         print("chiffre trop petit")
      else:
           print("exact")



from random import *
nombre = randint(1,20)
valeur=0
coups=0
while valeur != nombre:
      coups=coups+1
      print("votre chiffre")
      valeur=int(input("choisi un chiffre"))
      if valeur>nombre:
         print("chiffre trop grand")
      elif valeur<nombre:
         print("chiffre trop petit")
      else:
           print("exact vous avez trouvé en" ,coups,"coups")

from random import *
nombre = randint(1,20)
valeur=0
coups=0
while valeur != nombre:
      coups=coups+1
      print("votre chiffre")
      valeur=int(input("choisi un chiffre"))
      if valeur>nombre:
         print("chiffre trop grand")
      elif valeur<nombre:
         print("chiffre trop petit")
      else:
           print("exact vous avez trouvé en" ,coups,"coups")
      int(input("voulez vous rejouer"))


def compte(max):
    for n in range(0,max+1):
        print(n,end='')

compte(5)
print()
compte(8)

"""

