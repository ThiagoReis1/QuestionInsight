n1 = int(input(""))
a = n1 // 100
b = n1 % 100
if (n1 == (a+b)**2):
	mensagem = "atende"
else: 
	mensagem = "nao atende"
	
print(n1)
print(mensagem)