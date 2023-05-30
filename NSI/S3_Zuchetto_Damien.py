# Créé par damien.zuchetto, le 17/01/2023 en Python 3.7

#Sujet 3:
codeMorseLettres=['.-','-...','-.-.','-..','.','..-.','--.','....','..',
           '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
           '...','-','..-','...-','.--','-..-','-.--','--..']
codeMorseChiffres =['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']


texte=str(input("votre texte ?"))
texte=str(texte.upper())
textemorse=''
for i in range (len(texte)):
    if texte[i]>'A' and texte[i]<='Z':
        textemorse=codeMorseLettres[ord(texte[i])-65]
    elif texte[i]>'0' and texte[i]<='9':
        textemorse=codeMorseChiffres[ord(texte[i])-48]
    print(textemorse)



#Ex 4.3:

def double(texte):
    doubleur=''
    for i in range(len(texte)):
        texte.append(texte)
print(double("bon"))