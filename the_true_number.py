# importation des modules

import random
import sys

# mise en place de la variable random

random_number = random.randint(1,100)
saisie1 = input

# $----------------------debut du programme---------------------------$

while not saisie1 == random_number:
    saisie1 = input("Saisissez un nombre entre 1 et 100 : ")
    try: 
        saisie1 = int(saisie1)
    except:
        print("Saisissez un nombre valide ( un entier ) compris entre 1 et 100")
        sys.exit()
    if saisie1 < random_number:
        print("Le nombre random est plus grand")
    elif saisie1 > random_number:
        print("Le nombre random est plus petit")
    else:
        print("Gagné ! Vous avez trouvé le nombre correspondant")
        sys.exit()