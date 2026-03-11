x = float(input())
k = int(input())

cont = 0
acum = 0

while cont != k:
	if k>0:
		acum = acum + (x**(2*cont+1))/(2*cont+1)
		cont = cont + 1

print(round(acum, 7))