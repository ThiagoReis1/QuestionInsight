from math import*
x = float(input("x:"))
k = int(input("k:"))
cont = 1
serie = 1
while (cont < k):
	serie = serie + x**cont/factorial(cont)
	cont = cont + 1			
print(round(serie,9))
				 