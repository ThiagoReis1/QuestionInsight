from numpy import*
a = float(input("area a ser fertilizada: "))

if 0 <= a <= 10000:
	valor = a * 6.0 + 100.0
elif 10000 <= a <= 20000:
	valor = a * 5.50 + 150.0
elif 20000 <= a <= 30000:
	valor = a * 5.0 + 200.0
elif a > 30000: 
	valor = a * 4.5 + 250.0

print(round(valor, 2))
	

	
	