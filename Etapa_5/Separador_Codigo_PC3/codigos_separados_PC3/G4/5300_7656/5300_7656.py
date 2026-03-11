v = float(input("Informe a velocidade do peao: "))

while(v>=50):
	print(round(v,2))
	if(v>=50):
		v = v - (v * 0.25)
		
