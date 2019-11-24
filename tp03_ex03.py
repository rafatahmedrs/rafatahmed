import math
###    Copiez votre code de l'exercice précédent
# Fonctions
def initialisation_lapins() -> int:
    """
    :return:  # qui retournera un int # sans parametère,
    # représentant le nombre de lapins saisi par l’utilisateur
    """
    lapins_dep: int = 0
    while lapins_dep < CONDITION_LAPIN:
        lapins_dep = (int(input("Combien de lapins au départ (>=5)? ")))

    return lapins_dep


def initialisation_renards() -> int:
    """
    :return:  # et qui retournera un int # sans parametère,
    représentant le nombre de renards saisi par l’utilisateur
    """
    renard_dep: int = 0
    while renard_dep < CONDITION_RENARDS:
        renard_dep = (int(input("Combien de renards au départ (>=2)? ")))

    return renard_dep


### Déclaration et Initialisation des variables
CONDITION_LAPIN: int = 5
CONDITION_RENARDS: int = 2
EVALUATION: int = 50
taux_croissance_lapins: float = 0.4
taux_attaque: float = 0.01
taux_croissance_renards: float = 0.008
taux_mortalite: float = 0.1
inferieur_zero = 0.0

nb_renards: float = initialisation_renards()
nb_lapins: float = initialisation_lapins()

en_dessous_cinq_lapin: bool = False
en_dessous_cinq_renard: bool = False
remonte_cinq_lapin: bool = False
remonte_cinq_renard: bool = False
en_dessous_deux_lapin: bool = False
en_dessous_deux_renard: bool = False
# Programme Principal

def simulation(EVALUATION, nb_lapins, nb_renards):
    for mois in range(EVALUATION):
        mois += 1
        ancien_lapins = nb_lapins
        nb_lapins = nb_lapins * (1.0 + taux_croissance_lapins - taux_attaque * nb_renards)
        nb_renards = nb_renards * (1.0 + taux_attaque * ancien_lapins * taux_croissance_renards - taux_mortalite)
        if mois == EVALUATION:                  ###j'arrondis vers le bas à l'aide de math.floor
            print("Après", mois, "mois,", "Il y a ", abs(math.floor(nb_lapins)), "lapins", "et", abs(math.floor(nb_renards)),
                  "renards")
        if nb_lapins < 5:
            en_dessous_cinq_lapin = True    ##Si le nombre de lapins est inferieur a 5
        if nb_renards < 5:
            en_dessous_cinq_renard = True   ##Si le nombre de renards est inferieur a 5
        if nb_lapins < 2:
            en_dessous_deux_lapin = True
            nb_lapins = 0                   ##Si le nombre de lapin est inferieur a 2 on met 0
        if nb_renards < 2:
            en_dessous_deux_renard = True
            nb_renards = 0                  ##Si le nombre de lapin est inferieur a 2 on met 0
    if en_dessous_cinq_lapin is True:
        print("Les lapins ont été en voie d’extinction ")   ## si c'est vrai
        if en_dessous_deux_lapin is True:
            print("et les lapins ont disparus :-(")         ## si c'est vrai
    if en_dessous_cinq_renard is True:
        print("Les renards ont été en voie d’extinction ")  ## si c'est vrai
    if en_dessous_deux_renard is True:
        print("et les renards ont disparus :-(")
    elif en_dessous_cinq_lapin and en_dessous_cinq_renard is False: ## si c'est faux
        print("Les lapins et les renards ont des populations stables.")

### Séquence d'opérations
simulation(EVALUATION, nb_lapins, nb_renards)
