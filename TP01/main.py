import getopt
import sys

# initialisation des variables avec des valeurs par défaut
fichier = 'fichier_defaut.txt'
message = 'vide'
message_fin = 'fin vide'
repetition = 1

# mise en place des flags
try:
    opts, args = getopt.getopt(sys.argv[1:], "f:e:m:p:n", ["help", "print"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)
repetition = 1

# Recuperer valeur des arguments
for o, a in opts:
    if o == "-m":
        message = a
    elif o == "-f":
        fichier = a
    elif o == "-e":
        message_fin = a
    elif o == "-n":
        repetition = int(a)
    elif o in ("-p", "--print"):
        print(sys.argv[1:])
    elif o == "--help":
        print("help")
        sys.exit()
    else:
        assert False, "option fausse"

# vérifier argument non null
if message == 'vide' or message_fin == 'fin vide':
    print("Erreur : Veuillez fournir tous les arguments nécessaires.")
    sys.exit(2)

# enregistrer
with open(fichier, "a") as f:
    for i in range(repetition):
        f.write(f"{message}\n")
    f.write(f"\n{message_fin}")
    print(f"Les arguments ont été enregistrés dans le fichier '{fichier}' avec succès.")


""" 
    Une erreure de convertion depuis le string empeche de choisir le nombre de répétition
    Je n'ai pas trouver de solution
"""