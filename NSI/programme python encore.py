def occurence(tab,n):
    nb_occurence=0
    for i in range(len(tab)):
        if tab[i]==n:
            nb_occurence+=1
    return nb_occurence

print(occurence([1,2,3,2,8,2],2))

def max(tab):
    max=tab[0]
    for i in range(len(tab)):
        if tab[i]>max:
            max=tab[i]
    return max
print(max([2,6,7,3,4,2,5]))

def moyenne(tab):
    if len(tab)==0:
        print("erreur")
    somme=0
    for i in range (len(tab)):
        somme+=tab[i]
    moyenne=somme//len(tab)
    return moyenne
print(moyenne([2,5,8]))