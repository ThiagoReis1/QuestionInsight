a = float(input("primeira nota: "))
b = float(input("segunda nota: "))
c = float(input("terceira nota: "))
d = float(input("quarta nota: "))
e = float(input("quinta nota: "))
media = (a + b + c + d + e)/ 5
if(media >= 5):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(round(media,1))
print(mensagem)