# UNIVERSIDADE FEDERAL DO AMAZONAS UFAM
# NOME: NANCY FREITAS DA SILVA
# DATA: 29/06/2016
# PROGRAMA: NÚMERO CARACTERÍSTICO

x = int(input("Digite um número: "))
n1 = x // 1000
n2 = x % 1000
resposta = (n1 + n2) ** 2
if(x == resposta):
	print(x,"atende a propriedade")
else:
	print(mensagem)