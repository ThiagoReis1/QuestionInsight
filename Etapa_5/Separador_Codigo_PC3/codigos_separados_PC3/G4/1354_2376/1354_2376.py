#Importar modulo
from math import*

#Media de watts 
m = float(input("Digite a media de watts:"))

#Raio
r = float(input("Digite o raio:"))

#Area do circulo
A = pi * (r ** 2)

#Area iluminada
p = A * m 

#Impressao do resultado
print(round(p, 2))