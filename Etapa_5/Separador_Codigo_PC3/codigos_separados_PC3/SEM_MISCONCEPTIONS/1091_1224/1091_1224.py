numero = int(input("digite um numero"))
digitos1e2 = numero // 100
digitos3e4 = numero % 100
soma = (digitos1e2 + digitos3e4)**2
if (soma == numero):
		print(numero, "atende a propriedade")
else:
		print(soma)
		