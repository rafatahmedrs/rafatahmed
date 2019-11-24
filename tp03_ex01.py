from mots_pendus import tirer_mot

#Fonctions
def affichage_mot_cache (MOT,tirage,NB_ERRUER):
    """
    fonction qui prends en paramètres le mot caché, les lettres déjà tirées et le nombre d’erreurs restant
    :param MOT:str le mot cache
    :param tirage:str la lettre tirée
    :param NB_ERRUER:int le nombre d'erreur restant
    :return:
    """
    mot = MOT
    for i in range(mot):
        i +=  1

stock_let: str = ""
def tirage_lettre (Mot):
    """
    fonction fonction demandera à l’utilisateur de saisir une lettre
    et reposera la question tant que la lettre entrée a déjà été choisie
    :param Mot: le mot choisi
    :return:str retoune une lettre
    """
    stock_u = str(input("Veuillez entrer une lettre que vous n'avez pas choisie avant : "))
    while stock_let == stock_u:
        stock_u = str(input("Veuillez entrer une lettre que vous n'avez pas choisie avant : "))
    stock_u = stock_let
    return stock_u


def verification_mot (MOT)->bool:
    """
    fonction de varification qui retournera un booléen si le mot a été trouvé ou non
    :param MOT:le mot tiré
    :return:bool True or Falase
    """


def diminuer_erreurs (NB_ERRUER)->int:
    while NB_ERRUER > 1:
        resl = NB_ERRUER - 1
    return resl

#Programme principal
### Déclaration et Initialisation des variables
MOT: str = tirer_mot()
tirage: str = tirage_lettre ()
ESSAIE_JOUEUR: int = 0
NB_ERRUER:int = 10
### Séquence d'opérations
affiche: str = affichage_mot_cache(MOT,tirage,NB_ERRUER)