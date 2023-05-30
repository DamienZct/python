# Créé par damien.zuchetto, le 13/12/2022 en Python 3.7
#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    for i in range(0,len(matieres)):
        somme+=notes[i]*coefficients[i]
    return somme
print( "le nombre de points total est de", calculMoyenne(coefficients,notes))

def traitementBac(moyenne):
    moyenne/=100
    print ("Votre moyenne est de",moyenne)
    if moyenne>=0 and moyenne<8:
        print("dommage, pas le bac")
    elif moyenne>=8 and moyenne<10:
        print("dernière chance, rattrapage")
    elif moyenne>=10 and moyenne<12:
        print("ça passe, BAC sans mentions")
    elif moyenne>=12 and moyenne<14:
        print("cool, Mention assez bien")
    elif moyenne>=14 and moyenne<16:
        print("t chaud, mention bien")
    elif moyenne>=16 and moyenne<20:
        print("prends des douches stp, mention tres bien")
    else:
        print("veuillez entrer un chiffre compris entre 0 et 20")

def rechercheNoteMin(notes):
    min=notes[0]
    for b in range(0,len(notes)):
        if notes[b]<min:
            min=notes[b]
    print("la pire note est",min, "/20")
    return min


def rechercheNoteMax(notes):
    max=notes[0]
    for b in range(0,len(notes)):
        if notes[b]>max:
            max=notes[b]
    print("la pire note est",max, "/20")
    return max

def rechercheNote(notes,matieres,laNote):
    compteur=0
    notechercher=12
    for i in range(0,len(notes)):
        if notes[i]==notechercher:
            compteur+=1
    print("Vous avez eu", notechercher,"dans la matiere", matieres[1])
    print("vous avez eu", notechercher,"dans", compteur, "matieres")

def changeNote(notes):
    for n in range(0,len(notes)):
        notes=-1
        while (note<0 or note>20):
            print("quelle est votre note en",matieres[n])
            note=float(input())
        notes[h]=note
    pass


def tableauBac(coefficients,notes,matieres):
    for i in range(cote1,cote2):
        print("Votre note en ")
    pass


#changeNote(notes)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,12)
tableauBac(coefficients,notes,matieres)

#line_chart = pygal.HorizontalBar()
#line_chart.title = 'Notes du Bac (/20)'
#a completer question 8

#line_chart.render_to_file('notes.svg')


