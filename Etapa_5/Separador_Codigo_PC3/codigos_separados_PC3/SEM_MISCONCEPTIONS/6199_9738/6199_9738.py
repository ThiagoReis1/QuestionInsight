alt= float(input())
taxa = float(input())

altura_cicero = 1.8
taxa_cicero = 0.01

cont= 0

while (alt <= altura_cicero):
	cont= cont + 1
	alt= alt + taxa
	altura_cicero= altura_cicero + taxa_cicero
print(cont)
