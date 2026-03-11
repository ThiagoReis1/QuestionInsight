n1 = float(input("qual a primeira nota?"))
n2 = float(input("qual a segunda nota?"))
n3 = float(input("qual a terceira nota?"))
n4 = float(input("qual a quarta nota?"))
nm = (n1 + n2 + n3 + n4) / 4
if(nm>=6):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(round(nm, 1))
print(mensagem)