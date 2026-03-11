# UNIVERSIDADE FEDERAL DO AMAZONAS UFAM
# NOME: NANCY FREITAS DA SILVA
# DATA: 29/06/2016
# PROGRAMA: MÉDIA ARITMÉTICA

nota1 = float(input("Digite a nota parcial 1: "))
nota2 = float(input("Digite a nota parcial 2: "))
nota3 = float(input("Digite a nota parcial 3: "))
nota4 = float(input("Digite a nota parcial 4: "))
nota5 = float(input("Digite a nota parcial 5: "))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(round(media,2))
if(media >= 6.00):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(mensagem)