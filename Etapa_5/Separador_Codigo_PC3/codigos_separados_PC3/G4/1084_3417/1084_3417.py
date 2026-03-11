n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))

ma = (n1 + n2 + n3 + n4)/4

if(ma>=6): 
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"

print(round(ma, 1))
print(mensagem)
