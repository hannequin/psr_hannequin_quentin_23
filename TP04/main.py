"""
T04 : un script qui ajoute (attention il n'ecrit pas juste en écrasant tout) 
"hello world", dans un fichier et ajoute une ligne de retour à la fin de la chaîne de caractères
"""

import sys

try:
    fichier = sys.argv[1]
    test_fichier = open(fichier)
except IndexError:
    print('Entrer un nom de fichier')
except OSError:
    print('Nom non valide')

with open(fichier,"a" ) as f:
    f.write("Hello World\n")
