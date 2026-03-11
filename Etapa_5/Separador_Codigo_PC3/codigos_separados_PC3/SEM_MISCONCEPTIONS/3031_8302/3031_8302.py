
valor = float(input("valor de x: "))

if valor <= 1 and valor < 2 :
	f = 1
	
elif valor > 1 and valor <= 2:
	f = 2

elif valor > 2 and valor <= 3:
	f = valor**2

else:
	f = valor**3
	
print(round(f, 2))
	