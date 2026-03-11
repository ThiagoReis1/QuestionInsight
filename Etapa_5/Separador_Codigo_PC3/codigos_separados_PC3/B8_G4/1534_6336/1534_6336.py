from math import*

x = float(input("escreva um valor pra x: "))
k = int(input("escreva um valor interio: "))

# termo geral valores são elevados e fracionados pelo mesmo numero
i = 3 
cont = 0

while x > -1 and x < 1 and k > 0 and cont <= k:
	if k == 1:
		z = x
		print(x)
		cont = cont + 2
		
	elif k > 1:
		
		z = x + (x**i/i)
		z = z + (x**i/i)
		i = i + 1 
		cont = cont + 1
		
print(round(z, 7))
		
	