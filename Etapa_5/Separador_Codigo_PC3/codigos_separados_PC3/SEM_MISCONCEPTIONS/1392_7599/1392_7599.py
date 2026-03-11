consumo = float(input("consumo:"))
if(consumo<10):
	msg = (3*consumo)+ 30
else:
	msg = (3.5*consumo)+30
print(round(msg,2))