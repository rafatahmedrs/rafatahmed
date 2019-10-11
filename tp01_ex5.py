"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration des variables
prx_n_bill: int
rab_et: int
rab_mm: int
ff_fam: int
pri_pa: int
cart_m: int

cart_mll: str
cart_mm: str
cart_et: str
f_fam: str

### Initialisation des variables
prx_n_bill = 10
rab_et = 2
rab_mm = 3
ff_fam = 1
cart_m = 0
pri_pa = ""


### Séquence d'opération

cart_mll = str(input("Possédez-vous la carte mensuelle ? (oui ou non) "))

cart_mm = str(input("Possédez-vous la carte memebre ? (oui ou non) "))

cart_et = str(input("Possédez-vous la carte étudiante ? (oui ou non) "))

f_fam = str(input("Bénéficiez-vous du forfait famille ? (oui ou non ) "))

#Calcul du forfait
#Carte de memebre

if cart_m == "oui" and cart_et == "oui":
    pri_pa = prx_n_bill - rab_mm - rab_et
elif cart_et == "oui" and f_fam == "oui":
    pri_pa = prx_n_bill - 0
elif cart_m == "oui" and f_fam == "oui":
    pri_pa = prx_n_bill - rab_mm - ff_fam
elif cart_mll == "oui":
    pri_pa = prx_n_bill - 10
elif cart_mll == "oui" and cart_et == "oui" and f_fam == "oui":
    pri_pa = prx_n_bill - rab_mm - rab_et


print("Le prix a payer est :".format(pri_pa))







if cart_mll == "oui":
    print(cart_m)