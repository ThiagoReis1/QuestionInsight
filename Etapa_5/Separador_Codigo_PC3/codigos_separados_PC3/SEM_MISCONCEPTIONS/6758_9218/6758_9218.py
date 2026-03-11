# faça seu código aqui!

dia = float(input("determine a quantidade de dias alugados"))

if dia < 7: 
	total = (dia * 100) + 15
	print(total)
elif dia == 7: 
	total = (dia * 100) + 12
	print(total)
else: 
	total = (dia * 100) + 10
	print(total)