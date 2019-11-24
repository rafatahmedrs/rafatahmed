# Fonctions
def demander_annee() -> int:
    """
    une fonction qui ne prends pas de paramètres et retourne un entier
    :return:int l'année
    """
    anne_ = int(input("Entrer une année(1583-4000): "))
    while anne_ < 1583 or anne_ > 4000:
        anne_ = int(input("Entrer une année(1583-4000): "))
    return anne_


def affiche_date(annee, jour):
    """
    une fonction qui prend deux entiers en paramètres : une année et un chiffre entre 22 et 56
    :param annee: int qui reprente l'année
    :param jour:int qui reprenste le jour de paques
    :return: int affiche la date de paques
    """
    if jour < 31:
        print("Date de Paques en", annee, ":", jour, "Mars")
    else:
        resl = jour - 31
        print("Date de Paques en", annee, ":", resl, "Avril")


# Programme Principal
def date_paques(annee) -> int:
    jour: float = e + d + 22
    if e == 6 and (d == 29 or d == 28) and 11 * (m + 1) % 30 < condition:
        jour -= 7

    return jour

### Déclaration et Initialisation des variables
annee: int = demander_annee()
siecle = annee // 100
p = (13 + (8 * siecle)) // 25
q: float = siecle // 4
m: float = (15 - p + siecle - q) % 30
n: float = (4 + siecle - q) % 7
d: float = (m + (19 * (annee % 19))) % 30
e: float = (2 * (annee % 4) + 4 * (annee % 7) + 6 * d + n) % 7
condition: int = 19
jour: int = date_paques(annee)

### Séquence d'opérations

date_paques(annee)  ## j'insere la date pour le calcule du jour
affiche_date(annee, jour) ## j'insere l'année et le jour
