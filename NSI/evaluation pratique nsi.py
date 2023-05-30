# Créé par damien.zuchetto, le 09/05/2023 en Python 3.7

def renverse(mot):
        inversion = ""
        for i in range (0, len(mot)):
            mot= inversion+mot
        return mot
print(renverse("informatique") ) #"euqitamrofni"


