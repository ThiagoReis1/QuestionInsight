#entradas dos parametros
item = input("T ou S: ")
qnt_item = int(input("Quantos itens sao?: "))
acai  = int(input("Quantidade de acai: "))

if item.upper() == "T" :
	total = qnt_item * 5.50 + acai * 10
else:
	total = qnt_item *4.00 + acai * 10
	
print(round(total,2))