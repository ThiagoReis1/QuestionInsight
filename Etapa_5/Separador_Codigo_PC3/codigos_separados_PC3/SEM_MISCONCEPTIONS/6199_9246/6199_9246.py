cicero = 1.8
crescimento = 0.01

pessoa = float(input("digite altura: "))
crescimento_pessoa = float(input("digite crescimento: "))

anos = 0

while(pessoa <= cicero): 
	pessoa += crescimento_pessoa
	cicero += crescimento
	anos += 1

print(anos)