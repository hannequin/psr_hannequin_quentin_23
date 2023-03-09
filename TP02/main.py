""" 
écrire un programme qui print un emoji 
et qui l'écrit le nombre de fois voulu mais minimum 3 fois et maximum 15 fois et par défault en print 5 😋
"""
import argparse

parser = argparse.ArgumentParser(
                    prog = 'Affiche_emoji',
                    description = 'Programme qui affiche des emojis',
                    )

parser.add_argument("emoji", type=str)
parser.add_argument('--nombre', type=int, default=5, choices=range(3, 15))
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()
for i in range(args.nombre):
    print(args.emoji, end='')