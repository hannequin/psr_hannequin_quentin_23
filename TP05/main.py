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
except OSError:
    print('Nom non valide')

with open(fichier,"r" ) as f:
    contenu = f.readlines()
    for i in range(len(contenu)):
        print(f"Ligne n°{i+1}, contenu: {contenu[i]}")
