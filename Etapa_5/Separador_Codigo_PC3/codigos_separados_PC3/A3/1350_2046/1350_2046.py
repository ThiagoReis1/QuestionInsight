from math import*

estimativa= float(input("digite quatidade de arvores: "))
semieixo_maior= float(input("semieixo maior: "))
semieixo_menor= float(input("semieixo menor: "))
area= pi * semieixo_maior * semieixo_menor
total= area / 0.04

print (round(total, 0))
