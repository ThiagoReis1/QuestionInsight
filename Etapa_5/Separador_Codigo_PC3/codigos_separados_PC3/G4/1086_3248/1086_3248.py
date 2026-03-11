n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

ma = ((n1 + n2 + n3) / 3)
if(ma >= 7.0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
	
print(round(ma, 1))
print(mensagem)