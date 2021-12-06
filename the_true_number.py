# importation des modules

import random
import sys

# mise en place des différentes variables

random_number = random.randint(1,100)
saisie1 = input
user_input = 0

# $----------------------debut du programme---------------------------$

while not saisie1 == random_number:
    user_input = user_input + 1
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
        print("Vous avez fais",user_input,"essais")
        sys.exit()