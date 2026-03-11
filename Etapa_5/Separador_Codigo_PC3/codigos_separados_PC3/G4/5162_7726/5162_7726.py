from math import * 
a = float(input("A estimativa de acaizeiros: "))
l = float(input("Comprimento da aresta: "))
ah = (3 * ( 3*(l**2))**0.5 )/ 2
qt = a * ah
print(int(qt))