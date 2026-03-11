pro1 = float(input())
pro2 = float(input())
pro3 = float(input())
pro4 = float(input())

ma = (pro1 + pro2 + pro3 + pro4)/4

if(ma >= 5.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
print(round(ma,2))
print(mensagem)