num = int(input())

a = num // 10000
rest_a = num % 10000

b = rest_a // 100
rest_b = num % 100

c = rest_b // 1

if (num == ((a**3) + (b**3) + (c**3))):
	mensagem = "atende"
	
else:
	mensagem = "nao atende"

print(mensagem)
print (num)