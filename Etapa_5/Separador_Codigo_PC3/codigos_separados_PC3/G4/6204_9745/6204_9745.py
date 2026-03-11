alm = 1.86
tam = 0.01

alt = float(input("altura do coelho:"))
taxa = float(input("taxa de crescimento:"))

cont = 0

while alt <= alm:
	alt = alt + taxa
	alm = alm + tam
	cont = cont + 1
	
print(cont)