a = float(input("nota da prova 1: "))
b = float(input("nota da prova 2: "))
c = float(input("nota da prova 3: "))
d = float(input("nota da prova 4: "))
e = float(input("nota da prova 5: "))
x = (a + b + c + d + e)/ 5

if(x >= 7.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao por nota"
	
print(round(x, 2))
print(mensagem)