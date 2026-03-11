# Hanna Soares Rodrigues - 21650885
# Avaliacao 04
# Exercicio 01

quantidade = int(input("Qual a populacao inicial? "))
taxa = float(input("Qual a taxa anual de crescimento? "))
retirada = int(input("Qual o numero de tambaquis retirados anualmente? "))

soma = quantidade
t = taxa/100
contador = 0


while (soma > 0):
	soma = (soma + (soma * t)) - retirada
	contador = contador + 1

print(contador)
	