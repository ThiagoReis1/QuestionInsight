num = int(input("numero fornecido:"))

a = (num // 10000)
b = (num // 100) % 100
c = num % 100


soma = (a**3) + (b**3) + (c**3)

if (soma == num):
     mensagem = "atende"
else:
	  mensagem = "nao atende"
	
print(mensagem)
print(num)