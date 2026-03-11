hc = float(input("altura do coelho:"))
tc = float(input("taxa de crecimento do coelho:"))

altura_macaco = 1.86
taxa_macaco = 0.01
cont = 0
soma = 0


while hc < altura_macaco:
	altura_macaco = (altura_macaco + taxa_macaco)
	hc = (hc + tc)
	cont = cont + 1

print(cont)
	
	