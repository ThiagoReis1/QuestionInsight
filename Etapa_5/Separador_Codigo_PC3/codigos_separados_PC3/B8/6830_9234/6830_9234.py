produtos = input("digite a sequencia de produtos(Hortifruti=H, Laticinios=L, Enlatados=E): ")

preco_t = 0

for i in range(len(produtos)):
	if produtos[i] == 'H':
	   preco_t += 3.85
	elif produtos[i] == 'L':
	   preco_t += 2.95
	elif produtos[i] == 'E':
	   preco_t += 7.90
		
preco_t = round(preco_t,2)

print(preco_t)
