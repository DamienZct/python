def distance(v):
    rapport=0.01*v**2+0.28*v
    return(round(rapport,2))
    print(distance)

def somme_cube(a,b):
    rapport=a*a*a+b*b*b
    return(round(rapport))
    print(somme_cube)

def soldes(prix, taux) :
  reduc= prix* taux
  prixsolde= prix - reduc
  augmentation= prixsolde * aug
  return (reduc, prixsolde)

def TTC(TVA,HT):
    TTC= HT + HT/100 *TVA
    return(round(TTC))
    print(TTC)

from math import*
def hyp(a,b) :
  c =a*a+b*b
  return (c)

def peri(a,b):
    c =a*a+b*b
    racine=sqrt(c)
    perim=a+b+racine
    return(perim, racine)
    print(peri)

