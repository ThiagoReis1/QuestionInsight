from math import*
ang = radians(float(input("Angulo de lancamento:")))
v00 = float ( input("Velocidade inicial:"))
v0 = v00 ** 2
sim = sin(2 * ang)
d = v0 * sim / 9.8
print(round(d,2))