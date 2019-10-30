"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
""
programme qui gère la caisse d'un distributeur
"""


### Déclaration des variables
entre_monaie: float
rendu: int
produit_choisi: int
Sandwich_au_poulet: float
chips_paprika: float
barre_chocolat: float
Bonbons: float
ice_Tea: float
limonade: float
re_demande: bool
prix_produit = float
###Initialisation des variables
entre_monaie = (0)
sandwich_au_poulet = 4.90
chips_paprika = 2.50
barre_chocolat = 2.00
Bonbons = 3.30
ice_Tea = 2.20
limonade = 1.90
re_demande = False
prix_produit = 0
rendu = 0
###Séquence d'opération
"""Affichage des produits"""
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

#Demande de choisir le produit
produit_choisi: int = int(input("Veuillez sélectionner un produit et votre offre promotionnelle : "))
#Demande de choisir le prix
entre_monaie = float(input("Veuillez introduire votre monnaie : "))

#Calcule de prix
#Poulet

## Enter no valabale



while produit_choisi <1 and prix_produit > 6:
      print("Le produit sélectionné n'existe pas")

produit_choisi: int = int(input("Veuillez sélectionner un produit et votre offre promotionnelle : "))


    if produit_choisi == 1 and entre_monaie > sandwich_au_poulet :
            prix_produit = sandwich_au_poulet - entre_monaie
            rendu = entre_monaie - Sandwich_au_poulet


# Chips

    if produit_choisi == 2 and entre_monaie > chips_paprika:
        prix_produit = chips_paprika
        rendu = entre_monaie - prix_produit

#Calcule de prix
#Cohco

    if produit_choisi == 3 and entre_monaie > barre_chocolat:
        prix_produit = barre_chocolat
        rendu = entre_monaie - prix_produit

#Calcule de prix
#Bonbon
    if produit_choisi == 4 and entre_monaie > Bonbons:
        prix_produit = barre_chocolat
        rendu = entre_monaie - prix_produit

#Calcule de prix
 #Ice_Tea
    if produit_choisi == 5 and entre_monaie > ice_Tea:
        prix_produit = ice_Tea
        rendu = entre_monaie - prix_produit
    if produit_choisi == 5 and entre_monaie < barre_chocolat:


#Calcule de prix
#Limo
    if produit_choisi == 6 and entre_monaie > limonade:
       prix_produit = limonade
       rendu = entre_monaie - prix_produit

#Calcule de prix
#barre
 while entre_monaie < prix_produit:
    print("")




