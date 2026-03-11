altura_cicero = 1.8
taxa_cicero = 0.01

contador = 0

altura_pessoa = float(input("Informe a altura: "))
taxa_pessoa = float(input("Informe a taxa: "))

while altura_pessoa <= altura_cicero:
	altura_pessoa = altura_pessoa + taxa_pessoa
	altura_cicero = altura_cicero + taxa_cicero
	contador = contador + 1
print(contador)