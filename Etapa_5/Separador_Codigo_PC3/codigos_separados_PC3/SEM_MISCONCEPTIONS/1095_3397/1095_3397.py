n1 = int(input("numero fornecido"))
num1 = n1 // 10000
num2 = n1 % 10000
conta = (num1+num2)**2
if(n1==conta):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(n1)
print(mensagem)