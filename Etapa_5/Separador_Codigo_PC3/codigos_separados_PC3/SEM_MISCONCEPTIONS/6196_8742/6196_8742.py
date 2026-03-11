altura_chico = 1.5
taxa_chico = 0.02
altx = float(input("altura da pssoa: "))
tax = float(input("taxa de crescimento: "))
ano = 0
while altx < altura_chico:
	altura_chico = altura_chico + taxa_chico
	altx = altx + tax
	ano += 1
print(ano)