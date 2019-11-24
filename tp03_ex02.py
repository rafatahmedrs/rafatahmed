import math
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

# Programme Principal
def simulation(EVALUATION, nb_lapins, nb_renards):
        for mois in range(EVALUATION):
            mois += 1
            ancien_lapins = nb_lapins
            nb_lapins = nb_lapins * (1.0 + taux_croissance_lapins - taux_attaque * nb_renards)
            nb_renards = nb_renards * (1.0 + taux_attaque * ancien_lapins * taux_croissance_renards - taux_mortalite)
            if nb_lapins < 0:
                nb_lapins = 0
            if nb_renards < 0:
                nb_renards = 0
            print("Après", mois, "mois,", "Il y a ", abs(round(nb_lapins, 2)), "lapins", "et", abs(round(nb_renards, 2)), "renards")


### Séquence d'opérations
simulation(EVALUATION,nb_lapins,nb_renards)

