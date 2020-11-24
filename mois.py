#   ROmain GAUD
#   11/24/2020
#   Function: vDonne le nombre de jours exacts pour un mois

from bissextile import bissextile

def jours(mois,annee):
    mois31 = [1,3,5,7,8,10,12]
    mois30 = [4,6,9,11]
    if (type(mois)==int) or (type(annee)==int):
        if(mois <= 12) and (mois > 0):
            if mois in mois31:
                return 31
            elif mois in mois30:
                return 30
            elif bissextile(annee):
                return 28
            else:
                return 29
        else:
            print("Error : le parametre mois n'est pas compris entre 1 et 12 inclus")
            return 0
            
    else:
        print("Error : le parametre 'mois' ou 'annee' n'est pas un entier")
        return 0