n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

nt= (n1+n2+n3+n4)/4
if(nt >= 7):
	mensagem = ('Aprovado')
if(nt < 7):
	mensagem = ('Reprovado')
print(round(nt, 2))
print(mensagem)