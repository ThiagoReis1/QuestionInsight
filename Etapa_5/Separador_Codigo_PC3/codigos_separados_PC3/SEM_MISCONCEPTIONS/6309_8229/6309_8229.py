produtos = input("digite a string de produtos: ")
valor_total = 0.0
quantidade_hortifruti = 0
quantidade_cereais = 0
quantidade_laticinios = 0

for produto in produtos:
	if produto == "H":
		valor_total += 5.40
		quantidade_hortifruti += 1
elif produto == 'C':
	valor_total += 8.95
	quantidade_cereais += 1
elif produto == "L":
	valor_total += 4.50
	quantidade_laticinios += 1

valor_total = round(valor_total, 2)
print("valor total da compra: R$", valor_total)
print("quantidade de produtos dos hortifruti:", quantidade_hortifruti)
print("quantidade de produtos dos cereais:", quantidade_cereais)
print("quantidade de produtos laticinios:", quantidade_laticinios)