vel = float(input("Insira a velocidade de rotacao do piao lancado: "))
	
min = 0	

while vel >= 50:
	print(round(vel, 2))
	vel = vel - vel*.25
	min += 1
				

	
				
