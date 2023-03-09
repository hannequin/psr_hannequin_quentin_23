"""
TP06 : Écrire un script Python pour lire un fichier et créer un nouveau fichier 
qui ne contient que les lignes du fichier original qui ne contiennent pas une chaîne de caractères spécifique. 
"""
import argparse

parser = argparse.ArgumentParser(
                    prog = 'Copie_ligne',
                    description = 'Programme qui copie les lignes du fichier original sans les lignes avec chaines spécifié',
                    )

parser.add_argument("fichier")
parser.add_argument("-m", "--message", required=True)
parser.add_argument("-n", "--nouveau", required=True)

args = parser.parse_args()
# Ouvre le fichier de sortie en mode lecture, Ouvre le fichier de sortie en mode écriture
with open(args.fichier, 'r') as f_lit, open(args.nouveau, 'w') as f_ecrit:
    # Lire chaque ligne du fichier d'entrée
    for ligne in f_lit:
        # Vérifier si la ligne contient la chaîne de caractères spécifique
        if args.message not in ligne:
            # Écrire la ligne dans le fichier de sortie si elle ne contient pas la chaîne spécifique
            f_ecrit.write(ligne)
