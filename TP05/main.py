"""
T05 : Écrire un script Python pour lire un fichier ligne par ligne 
et imprimer chaque ligne avec un préfixe de numéro de ligne.
"""
import sys

try:
    fichier = sys.argv[1]
    test_fichier = open(fichier)
except IndexError:
    print('Entrer un nom de fichier')
#except OSError:
#    print('Nom non valide')

with open(fichier,"w" ) as f:
    contenu = f.read()
    f.write(f"{len(f.readline())}")
    # contenu = f.readline
    # for i in range(len(contenu)):
    #     f.write(f"{i+1} {contenu}")
