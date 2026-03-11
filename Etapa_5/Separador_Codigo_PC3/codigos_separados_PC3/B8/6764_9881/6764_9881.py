# faça seu código aqui!
pacote = float(input("e o pacote meu cumpadre: "))
 
if pacote < 5:
	total = 10.0 + 3.75
elif pacote == 5:
	total = 10.0 + 4.75
elif pacote > 5:
	total = 10.0 + 5.75
	
print(round(total, 2))

