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

###Initialisation des variables
entre_monaie = 0
entre_monaie = 4.90

sandwich_au_poulet = 4.90
chips_paprika = 2.50
barre_chocolat = 2.00
Bonbons_à = 3.30
ice_Tea = 2.20
limonade = 1.90
###Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")
entre_monaie = int(input("Veuillez introduire votre monnaie : "))
produit_choisi = int(input("Veuillez sélectionner un produit : "))

if produit_choisi == 1:
    if entre_monaie >= sandwich_au_poulet :
        print("Monnaie à rendre : " +str(entre_monaie - sandwich_au_poulet))
    else:
         print("monnaie insufisante")
if produit_choisi == 2:
    if entre_monaie >= chips_paprika:
        print("Monnaie à rendre : ",(entre_monaie-chips_paprika))
    else:
        print("monnaie insufisante")
if produit_choisi >= 3:
    if entre_monaie > barre_chocolat:
        print(entre_monaie-barre_chocolat)
    else:
        print("monnaie insufisante")
if produit_choisi >=4 :
    if entre_monaie > Bonbons:
        print(entre_monaie-Bonbons)
    else:
        print("monnaie insufisante")
if produit_choisi >= 5 :
    if entre_monaie >ice_Tea:
        print(entre_monaie-ice_Tea)
    else:
        print("monnaie insufisante")
if produit_choisi >= 6 :
    if entre_monaie > limonade:
        print(entre_monaie-limonade)
    else:
        print("monnaie insufiante")




