c1 = float(input("Qual o valor?"))
c2 = float(input("Qual o valor?"))
c3 = float(input("Qual o valor?"))
c4 = float(input("Qual o valor?"))
limite = float(input("qual o valor?"))
total = c1 + c2 + c3 + c4

if(total <= limite):
	mensagem = ("sim")
else:
	mensagem = ("nao")
print(round(total, 2))
print(mensagem)

