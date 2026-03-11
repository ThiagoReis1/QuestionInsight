# faça seu código aqui!
tipo= input("Digite o tipo do combo desejado: ").upper()
quant=int(input("Digite a quantidade de combos desejados: "))

if tipo == 'C':
	desc=15/100*(quant*30)
	total=(quant*30)-desc
	print(round(total,2))
else:
	total=quant*30
	print(round(total,2))