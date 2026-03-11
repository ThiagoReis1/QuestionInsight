n1 = float(input("n1:"))
n2 = float(input("n2:"))
n3 = float(input("n3:"))
n4 = float(input("n4:"))
n5 = float(input("n5:"))

media = (n1 + n2 + n3 + n4 +n5)/5
media_aritmetica = (n1 + n2 + n3 + n4 +n5)/5

if(media>=7.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
print(round(media_aritmetica,2))
print(mensagem)