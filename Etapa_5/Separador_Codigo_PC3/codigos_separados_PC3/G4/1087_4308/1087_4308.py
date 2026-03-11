a = float(input("nota um: "))
b = float(input("nota dois: "))
c = float(input("nota tres: "))
d = float(input("nota quatro: "))

m = (a + b + c + d) / 4
print(round(m,2))

if(m >= 7.0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(mensagem)