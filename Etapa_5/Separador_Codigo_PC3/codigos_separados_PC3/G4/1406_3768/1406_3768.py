at = input("digite o tipo de ataque")
N = int(input("digite o valor sorteado"))
t = int(input("digite o numero de turnos"))

if (at=="cuspe"):
	a = 2*N*t	
else:
	a = N*t

print (a)


