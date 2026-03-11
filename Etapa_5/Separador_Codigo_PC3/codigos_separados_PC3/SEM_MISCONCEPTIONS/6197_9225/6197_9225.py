altura_alice = 1.6
taxa_alice = 0.02

altura = float(input("altura da pessoa: "))
taxa_cresci = float(input("taxa de crescimento: "))
ano = 0

while altura < altura_alice:
	altura = altura + taxa_cresci
	altura_alice = altura_alice + taxa_alice
	ano = ano + 1

print(ano)

