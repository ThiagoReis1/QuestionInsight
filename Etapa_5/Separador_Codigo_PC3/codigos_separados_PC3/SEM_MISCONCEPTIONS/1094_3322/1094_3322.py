num = int(input())

num1 = num//1000
resto1 = num%1000
num2 = resto1

if (((num1+num2)**2) == num):
	mensagem = "atende"
else:
	mensagem = "nao atende"
		
print(mensagem)
print(num)