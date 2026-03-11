n1 = float(input("inferior a primeira nota:"))
n2 = float(input("inferior a segunda nota:"))
n3 = float(input("inferior a terceira nota:"))
n4 = float(input("inferior a quarta nota:"))
x = (n1 + n2 + n3 + n4) /4

if(x >= 6.0):
    mensagem = "Aprovado"
else:
	 mensagem = "Reprovado"
	
print(round(x, 1))
print(mensagem)

