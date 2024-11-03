# Exercice 7 : Compter les Caractères


#  Demandez à l'utilisateur d'entrer un mot.
#  Utilisez une boucle for pour compter combien de fois chaque caractère apparaît dans le mot.
#  Affichez le résultat sous la forme : "Le caractère 'x' apparaît y fois."
# Demander à l'utilisateur d'entrer un mot
mot = input("Entrez un mot : ")

# Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque caractère
compte_caracteres = {}

# Utiliser une boucle for pour compter combien de fois chaque caractère apparaît
for caractere in mot:
    if caractere in compte_caracteres:
        compte_caracteres[caractere] += 1  # Incrémenter le compteur si le caractère est déjà présent
    else:
        compte_caracteres[caractere] = 1  # Initialiser le compteur à 1 si le caractère est nouveau

# Afficher le résultat
for caractere, compte in compte_caracteres.items():
    print(f"Le caractère '{caractere}' apparaît {compte} fois.")
