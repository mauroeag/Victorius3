
class ParImpar:
    ArrayNumeros =[]
    def __init__(self, lista):
        self.ArrayNumeros = lista

    def add(self,number):
        self.ArrayNumeros.append(number)

    def sumaPar(self):
        suma=0
        for i in self.ArrayNumeros:
            if i % 2==0:
                suma +=i   
        return suma
    def sumaImpar(self):
        suma=0            
        for i in self.ArrayNumeros:
            if i %2 != 0:
                suma +=i
        return suma
    def cuadradoLista(self):
        ArrayCuadrado =[]
        for i in self.ArrayNumeros:
            ArrayCuadrado.append(i*i)
        return ArrayCuadrado    