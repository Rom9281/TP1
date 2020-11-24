#   Romain GAUD
#   11/24/2020
#   Fonction: verifier si une annee est bissextile ou non

def bissextile(annee):
    if type(annee) == int:
        if ((str(annee)[-2:] != "00") and (annee%4 == 0)) or (annee%400 == 0 ):
            return True
        else:
            return False
    else:
        print("Error : le parametre 'annee' n'est pas un entier")
        return 0