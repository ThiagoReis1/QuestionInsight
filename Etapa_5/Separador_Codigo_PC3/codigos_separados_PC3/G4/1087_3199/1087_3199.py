n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
ma = (n1+n2+n3+n4)/4
ma1 = round(ma,2)
if (ma1 >= 7.0):
	mensagem = "Aprovado"
else: 
	mensagem = "Reprovado"
	
print(ma1)
print(mensagem)