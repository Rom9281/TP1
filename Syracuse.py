class Syracuse():
    def __init__(self,depart = 1, nb_it = 20):
        self.__n = depart # le nombre de depart
        self.__it = nb_it #le nombre de nombres de la suite a afficher
    
    def verify(self,n):
        if (type(n) == int) and (n > 0):
            return True
        else:
            return False
    
    def calculate(self):
        if self.verify(self.__n) and self.verify(self.__it):
            n = self.__n
            liste = [n]
            for i in range(self.__it - 1):
                if n%2 == 0:
                    n = n/2
                else:
                    n = 3*n + 1
                liste.append(n)
            return liste
        else:
            print("Error : parametres 'depart' ou 'nb_it' n'est pas un entier positif")
    
    def max(self):
        return max(self.calculate())
    
    def temps_vol(self):
        liste = self.calculate()
        for i in range(1,len(liste)):
            if liste[i] == 1:
                return i + 1
        return 0
    
    def max_tv(self,inf,sup):
        max_tv = 0 
        for i in range(inf,sup):
            self.__n = i
            if self.temps_vol() > max_tv:
                max_tv = self.temps_vol()
                im = i
        return max_tv , im
    
    def max_alt(self,inf,sup):
        max_alt = 0
        for i in range(inf,sup):
            self.__n = i
            if self.max() > max_alt:
                max_alt = self.max()
                im = i
        return max_alt, im
        

syracuse = Syracuse(703,200)
print(syracuse.calculate())
print(syracuse.max())
print(syracuse.temps_vol())
print(syracuse.max_alt(1,1000))
print(syracuse.max_tv(1,1000))
                
        