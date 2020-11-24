#   Romain GAUD
#   11/24/2020
#   Fonction: calculer les impots en 2019

def mesImpots(revenus):
    tranches = [9964,27519,73779,156244]
    pourcent = [0,0.14,0.30,0.41,0.45]
    try:
        revenus = int(revenus)
        if revenus >= 0:
            if revenus < tranches[0]:
                return "Zero"
            else:
                due, i = Calc(revenus,tranches,pourcent)
                while i != 0:
                    i += -1
                    due += (tranches[i]-tranches[i-1])*pourcent[i]
                return due
        else:
            print("Error: le parametre 'revenus' n'est pas un entier positif")
            return False
    except ValueError:
        print("Error : le parametre 'revenus' n'est pas convertible en entier")

def Calc(revenus,tranches,pourcent):
    for i in range(1,len(pourcent)):
            if i == len(pourcent)-1:
                if revenus >= tranches[i - 1]:
                    return (revenus - tranches[i-1])*(pourcent[i]) ,i
            else:
                if (revenus < tranches[i]) and (revenus >= tranches[i-1]):
                    return (revenus - tranches[i-1])*(pourcent[i]),i 
    

print("\nCalcul  d'impots V.2019")
val = input("Revenu net : ")
if mesImpots(val):
    print("Le montant des impots : %s euros" %(mesImpots(val)))