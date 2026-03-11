from math import pi
from math import cos
raio= float(input("Inserir valor do raio: "))
lados= float(input("Inserir numero de lados: "))
a= raio*cos(pi/lados)
print(round(a,2))