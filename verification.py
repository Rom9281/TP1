#   Romain GAUD
#   11/24/2020
#   Fonction : verifier si une date est valide
from mois import jours

def verification(date): #sous format 'jj/mm/aaaa'
    l_date = date.split("/")
    if len(l_date) == 3:
        if (len(l_date[0]) == 2) and (len(l_date[1]) == 2):
            try:
                jour = int(l_date[0])
                mois = int(l_date[1])
                annee = int(l_date[2])
                
                if jours(mois,annee) != 0:
                    if (jour <= jours(mois,annee)) and (jour > 0):
                        return True
                    else:
                        return False
                else:
                    return 0
            except ValueError:
                print("Error : Le jour, le mois ou l'annee n'est pas un entier")
                return 0
            print("Error : l'annee, le mois ou le jour n'ont pas le bon nb de caracteres")
            return 0
    else:
        print("Error : parametre n'est pas un str sous la forme jj/mm/aaaa")
        return 0

print(verification('01/09/axert'))
    