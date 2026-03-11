km = float(input('kilometros'))

if(km < 10):
	taxa = 5.5
	
elif(km == 10):
	taxa = 7.75
	
else:
	taxa = 10.0
	
custo = 50 + taxa
print(round(custo, 2))