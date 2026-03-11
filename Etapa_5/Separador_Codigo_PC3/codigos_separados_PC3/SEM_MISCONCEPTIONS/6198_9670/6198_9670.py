alt=float(input("altura da pessoa: "))
tx=float(input("taxa de crescimento da pessoa: "))

altlu = 1.65
taxa_luna = 0.02
ano=0
while alt <= altlu:
	altlu=altlu+taxa_luna
	alt=alt+tx
	ano=ano+1
print(ano)












