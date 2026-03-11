num = int(input("valor com 4 digitos: "))

d1 = num // 100
d2 = num % 100

c = ((d1 + d2) ** 2)

if(c == num):
	mensagem = "atende"
else:
	mensagem = "nao atende"
	
print(num)
print(mensagem)