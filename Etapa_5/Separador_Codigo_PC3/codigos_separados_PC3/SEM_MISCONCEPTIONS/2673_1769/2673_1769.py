from math import sin, pi

raio = float(input())
num_lados = int(input())

lado_l = 2 * raio * sin(pi/num_lados)

print(round(lado_l, 2))