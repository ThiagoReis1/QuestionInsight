altura_chico = 1.5
taxa_chico = 0.02

f = float(input("altura: "))
t = float(input("taxa de crescimento: "))

a=0

while f < altura_chico:
	altura_chico = altura_chico + taxa_chico
	
	f += t
	a +=1

print(a)