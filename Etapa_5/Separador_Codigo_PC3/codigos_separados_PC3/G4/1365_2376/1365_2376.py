#Importar modulo 
from math import*

#Angulo da flecha ao sair do arco
a = float(input("Insira o angulo:"))

#Distancia entre o guerreiro e o Falmer
d = float(input("Insira a distancia:"))

#Constante G
g = 9.8 

#Velocidade inicial da flecha
v = sqrt(d * g/sin(2*radians(a)))

#Impressao da velocidade
print(round(v, 2))