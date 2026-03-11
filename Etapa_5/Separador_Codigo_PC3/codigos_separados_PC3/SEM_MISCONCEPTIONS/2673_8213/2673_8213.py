import math
raio=float(input("valor do raio r:"))
numero_de_lados=int(input("numero de lados:"))
lado_l=2*raio*math.sin(math.pi/numero_de_lados)
print(round(lado_l,2))