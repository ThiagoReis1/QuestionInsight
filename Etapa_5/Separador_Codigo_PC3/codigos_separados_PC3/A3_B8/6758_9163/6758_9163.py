# faça seu código aqui!
dia = int(input("Digite a quantidades de dias que deseja alugar um carro: "))
carro2 = 100
total = 0 
if dia < 7: 
	print(round(dia  * carro2 + 15 ,2))
	
elif dia == 7:  
	print(round(dia * carro2 + 12 ,2))
	
elif 	dia > 7:  
	print(round(dia * carro2 + 10 ,2))

