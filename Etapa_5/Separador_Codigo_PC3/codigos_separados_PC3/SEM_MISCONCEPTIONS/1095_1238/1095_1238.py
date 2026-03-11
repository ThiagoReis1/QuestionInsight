# Talita Passos
# Matricula - 21552161
# 30 de Junho de 2016
# Avaliacao 2 - Ex 2

numero = int(input("Digite um numero: "))

resultado = round(numero // 10000, 0)
resto = round(numero%10000, 0)

equacao = (resultado + resto)**2

if(numero == equacao):
	print("X atende a propriedade")
else:
	print(equacao)