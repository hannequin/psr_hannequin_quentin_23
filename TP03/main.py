"""
TP03 : écrire un script python pour lire et print le contenu d'un fichier 
"""
import sys

try:
    fichier = sys.argv[1]
    test_fichier = open(fichier)
except IndexError:
    print('Entrer un nom de fichier')
except OSError:
    print('Nom non valide')

with open(fichier,"r" ) as f:
    contenu = f.read()
print(contenu)
