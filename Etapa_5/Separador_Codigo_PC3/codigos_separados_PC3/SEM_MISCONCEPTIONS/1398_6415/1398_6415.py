tempo = float(input("Digite o tempo de voo:"))


if(tempo <= 200):
	c = (tempo * 100) + 5000
	
else:
	c = (8000 + 2000) + tempo * 90
	
print(round(c,2))