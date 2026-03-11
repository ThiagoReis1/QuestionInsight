# faça seu código aqui!
diasemana = input("dia da semana")
totalpratos = int(input("total de pratos"))
 
if diasemana == "qua":
	valorfinal = totalpratos - (22 * 0.15)
else:
	valorfinal = totalpratos * 22
	
print(round(valorfinal, 2))

