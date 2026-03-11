joe = 1.77
taxa_joe = 0.02

pessoa = float(input("altura da pessoa  "))
crescimento = float(input("taxa de crescimento  "))
cont= pessoa
ano = 0
while pessoa<joe:
	joe = joe + taxa_joe
	pessoa = pessoa + crescimento
	ano += 1
print(ano)
	