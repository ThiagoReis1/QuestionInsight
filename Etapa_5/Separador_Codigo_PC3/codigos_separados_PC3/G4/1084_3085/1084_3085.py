a = float(input("nota 1: "))
b = float(input("nota 2: "))
c = float(input("nota 3: "))
d = float(input("nota 4: "))

m = (a + b + c + d) / 4

if(m >= 6):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(round(m, 1))
print(mensagem)