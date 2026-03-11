a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())

media = (a+b+c+d+e)/5

if (media >= 7.0):
	mensagem= "Aprovacao"
else: 
	mensagem= "Reprovacao por nota"
print(round(media, 2))
print(mensagem)
	