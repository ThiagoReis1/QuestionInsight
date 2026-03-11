from math import*
raio = float(input("Qual o Raio? "))
n_raio = int(input("Numero de Raios? "))

apotema = raio * cos(pi/n_raio)

print(round(apotema, 2))