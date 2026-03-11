import math
raio_r = float(input("Raio: "))
n_lados = float(input("Numero de lados: "))
lado_L = 2*raio_r*math.sin(math.pi/n_lados)
print(round(lado_L,2))