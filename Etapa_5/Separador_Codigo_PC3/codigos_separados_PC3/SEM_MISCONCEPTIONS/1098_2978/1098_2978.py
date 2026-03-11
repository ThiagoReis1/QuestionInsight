n = int(input('Digite um numero inteiro: '))
inicial = (n // 1000)
final = (n % 1000)
print(n)
if ((inicial - final) ** 4) == n:
	print('atende')
else:
	print('nao atende')
