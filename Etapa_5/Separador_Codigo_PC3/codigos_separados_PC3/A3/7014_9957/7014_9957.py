# acumuladoras 
xis = int(input())
yis = int(input())
soma_impar = 0
control = 0
new_xis = 0

while new_xis <= yis:
	new_xis += xis + 1
	if xis %2 != 0:
		soma_impar += xis
	if new_xis %2 != 0:
		soma_impar += new_xis

if new_xis > yis:
	print(soma_impar)