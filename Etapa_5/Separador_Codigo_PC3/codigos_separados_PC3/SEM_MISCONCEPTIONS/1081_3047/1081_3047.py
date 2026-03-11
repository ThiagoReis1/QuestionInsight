a = float(input("primeira nota "))
b = float(input("segunda nota "))
c = float(input("terceira nota "))
d = float(input("quarta nota "))
media = ((a+b+c+d)/4.0)
if (media <= 5.0):
	mensagem = "Reprovacao"
else :
	mensagem = "Aprovacao"
print(round(media, 2))
print(mensagem)