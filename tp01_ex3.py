"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""


"""Programme calculant le niveau de risque cardiovasculaire """

### Déclaration des variables
age_utilisateur: int
sexe_utilisateur:bool
fumeur: str
fait_sport: bool
age_risque_homme: int
age_risque_femme: int
Oui: int
Non: int
### Initialisation des variables
fumeur = str(input('Etes-vous fumeur ? (Oui or Non) '))
fait_sport = bool(input("Faites-vous du sport  (Oui or Non) "))
sexe_utilisateur = bool(input("Quel est votre sexe (h ou f ) "))
age_utilisateur = int(input("Quel est votre âge ? :  "))
Oui = 2
Non = 0
risque_maximal = 3
### Séquence d'opération
#Calcul de risque
if fumeur == Non :
    if fait_sport == Oui :
