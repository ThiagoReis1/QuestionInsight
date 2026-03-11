from math import*

num = int(input("Digite um valor: "))

if(num == (num // 100)**2 + (num % 100)**2):
	print(num)
	print("atende a propriedade")
else:
	soma = (num // 100)**2 + (num % 100)**2
	print(soma)