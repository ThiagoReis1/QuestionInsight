from math import *
r = float (input("Qual o raio?"))
n = int (input("Quantos lados tem o poligono?"))
a = r * cos (pi / n)

print (float ( round (a , 2) ) )