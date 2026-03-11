from math import*
A =float(input("Quantidade de smowberry: "))
B = float(input("Quantidade de sais de fogo: "))
C = float(input("Quantidade de amanita: "))
snow = 0.31
fogo = 0.73
amani = 2.64
D = A/snow
E = B/fogo
F = C/amani
G =int(min(D,E,F))
print(G)