# faça seu código aqui!
dias= int(input("Quantos dias: "))
diaria= 100.00

if dias<7:
	aluguel= diaria*dias+15.0
elif dias==7:
	aluguel= diaria*dias+12.0
elif dias>7:
	aluguel= diaria*dias+10.0
	
print(round(aluguel, 2))