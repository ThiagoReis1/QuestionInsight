qta= int(input("Quantidade de votos A:"))
qtd= int(input("Quantidade de votos D:"))
total = qta+qtd
if(qta>qtd):
	print("Ambrosio Rutra")
	porcentagem = (100*qta)/total
else:
	print("Demelza Olecram")
	porcentagem = (100*qtd)/total
print(round(porcentagem, 2))