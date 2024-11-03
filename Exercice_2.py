# Exercice 3 : Jeu de Devine le Nombre
# Choisissez un nombre aléatoire entre 1 et 100 en utilisant
# import random et random.randint(1, 100)
# Demandez à l'utilisateur de deviner le nombre jusqu'à ce qu'il le trouve.
# Utilisez une boucle while pour permettre plusieurs tentatives et donnez 
# des indices ("trop grand" ou "trop petit")
import random

# Choisir un nombre aléatoire entre 1 et 100
nombre_a_deviner = random.randint(1, 100)

# Initialiser la variable de tentative de l'utilisateur
tentative = None

print("Essayez de deviner le nombre (entre 1 et 100) !")

# Boucle jusqu'à ce que l'utilisateur trouve le nombre
while tentative != nombre_a_deviner:
    # Demander à l'utilisateur de saisir un nombre
    tentative = int(input("Entrez votre devinette : "))

    # Vérifier si la tentative est correcte
    if tentative < nombre_a_deviner:
        print("Trop petit ! Essayez encore.")
    elif tentative > nombre_a_deviner:
        print("Trop grand ! Essayez encore.")
    else:
        print("Bravo ! Vous avez trouvé le nombre.")