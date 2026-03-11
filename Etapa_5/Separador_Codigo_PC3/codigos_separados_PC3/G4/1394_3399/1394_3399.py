x = float(input("numero de hora: "))

n1 = (x - 20)

if(x <= 20):
	caso = x*50
else:
	caso = (x*50)-(n1*50) + (n1*70)
print(round(caso, 2))