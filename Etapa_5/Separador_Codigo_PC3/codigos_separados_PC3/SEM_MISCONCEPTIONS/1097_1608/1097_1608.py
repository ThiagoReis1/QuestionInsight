# Victor Lopes Aguiar -     Matrícula - 21551604
# Avaliacao 02

X = int(input("Digite um numero com 6 digitos: "))

milhar = X // 1000

centena = X % 1000

diferenca = (milhar - centena)**2

if (X == diferenca):
	print (X, "atende a propriedade")
else:
	print (diferenca)