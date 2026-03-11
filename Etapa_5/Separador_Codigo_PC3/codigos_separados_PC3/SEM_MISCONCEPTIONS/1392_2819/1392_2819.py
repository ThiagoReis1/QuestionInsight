consumo = float(input(""))
if(consumo < 10):
	conta = 3*consumo
else:
	conta = (3.5)*consumo 
print(round((conta + 30), 2))