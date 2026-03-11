from math import*

raio_r = float(input("raio:"))
n_lados = int(input("n_lados:"))

prt1 = 2 * raio_r
prt2 = pi/n_lados
prt3 = sin(prt2)

l = prt1 * prt3

print(round(l,2))