# faça seu código aqui!
km = int(input("Informe a distancia em quilometros: "))

if(km<10):
	taxa = 50+5.50
	print("total=",round(taxa,2))
elif(km==10):
	taxa = 50+7.75
	print("total=", round(taxa,2))
else: 
	taxa = 50+10.0
	print("total=", round(taxa,2))
	