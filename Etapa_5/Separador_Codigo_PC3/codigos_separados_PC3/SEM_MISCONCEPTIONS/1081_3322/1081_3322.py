a = float(input())
b = float(input())
c = float(input())
d = float(input())

media = (a+b+c+d)/4

if (media>=5):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
	
print(round(media, 2))
print(mensagem)