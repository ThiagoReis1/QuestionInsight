from math import*

r = float(input("digite o raio: "))
n = int(input("digite numero de lado: "))
A=(1/2)*(((r*cos(pi/n)))**2)*(tan(pi/n))
print(round(A,2))