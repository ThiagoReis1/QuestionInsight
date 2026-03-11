# faça seu código aqui!
carros = float (input( "carros: " ))
if carros < 7 :
	taxa= carros * 100 + 15
elif carros == 7 :
	taxa= carros * 100 + 12
else: 
	taxa = carros * 100 + 10
	
print(round(taxa,2))