#  Romain GAUD
#  11/24/2020
#  Fonction : verifier la saisie de l'utilisateur
from verification import verification


print("\nEntrer ici une date sous la forme jj/mm/aaaa")
val = input("Date : ")
   
if verification(val):
    print("\n  -  La date %s est valide  -  "%(val,))
else:
    print("\n   - La date %s n'est pas valide - " %(val,))