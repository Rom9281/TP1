#   ROmain GAUD
#   11/24/2020
#   Objectif : realiser une multiplication de deux matrices carre
class matrice():
    def __init__(self,lignes = [0]):
        self.__lignes = lignes
        self.__dim = len(lignes)
    
    def getLigne(self,i):
        '''Retourne la ligne i | ATT! : i commence a 0'''
        return self.__lignes[i]
    
    def getColonne(self,i):
        colonne = []
        for n in range(len(self.__lignes)):
            colonne.append(self.getLigne(n)[i])
        return colonne
    
    def mul_vect(self,ligne, colonne):
        somme = 0 
        for i,l in enumerate(ligne):
            somme += l*(colonne[i])
        return somme
    
    def mul(self,M):
        '''Multiplication entre cete matrice et une matrice B'''
        #Premiere ligne permet de multiplier une ligne par les differentes colonnes
        C = []
        for i in range(self.__dim):
            c = []
            for j in range(self.__dim):
                c.append(self.mul_vect(self.getLigne(i),B.getColonne(j)))
            C.append(c)
        return C

A = matrice([[1,2,1],[2,1,5],[3,1,1]])
B = matrice([[1,0,0],[0,1,1],[0,0,1]])
print(A.mul(B))
                