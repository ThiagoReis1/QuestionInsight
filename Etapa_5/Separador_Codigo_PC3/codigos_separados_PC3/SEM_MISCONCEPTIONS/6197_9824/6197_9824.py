altura_alice = 1.6
taxa_alice = 0.02

altp = float(input("altura da pessoa: "))
taxap = float(input("taxa de crescimento: "))

ano = 0 

while altp < altura_alice:
	altp = altp + taxap
	altura_alice = altura_alice + taxa_alice
	ano = ano + 1
	
print(ano)