n1 = float(input("figite a nota: "))
n2 = float(input("digite a nota: "))
n3 = float(input("digite a nota: "))
n4 = float(input("digite a nota: "))
n5 = float(input("digite a nota: "))

soma = (n1 + n2 + n3 + n4 + n5)/5

if (soma >= 5.0):
	mensagem = "Aprovado"
	
else:
	mensagem = "Reprovado"
	
print(round(soma, 1))
print(mensagem)