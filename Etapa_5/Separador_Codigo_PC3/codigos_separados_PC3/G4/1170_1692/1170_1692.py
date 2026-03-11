from math import *

n = float(input("Insira o numero: "))

cont = 1


while(cont < n):
		den = (cont*2)*(cont*2+1)*(cont*2+2)
		ap = ap + (-1) ** (cont+1)*4/den
		cont = cont + 1
		
print(round(ap, 8))