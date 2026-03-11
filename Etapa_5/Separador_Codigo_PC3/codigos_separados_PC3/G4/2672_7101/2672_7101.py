from math import*
#Faça um programa que tenha como entrada:
#O raio r do polígono regular (número real)
r = float(input("raio r:"))
#O número de lados n (inteiro)
n = int(input("lados n:"))
#cálculo:
a = (1/2) * ((r * cos(pi/n))**2 * tan(pi/n))
print(round(a, 2))