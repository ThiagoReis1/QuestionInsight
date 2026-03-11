numeroprato = int(input())
numerosob = int(input())
numerobeb = int(input())

if numeroprato > 4 or numeroprato < 1 or numerosob > 4 or numerosob < 1 or numerobeb < 1 or numerobeb > 4:
	print("Entradas:" ,numeroprato, "," ,numerosob,",", numerobeb)
	print("Dados invalidos")
else:
	if numeroprato == 1:
		cal = 180
	elif numeroprato == 2:
		cal = 230
	elif numeroprato == 3:
		cal = 250	
	elif numeroprato == 4:
		cal = 350
	if numerosob == 1:
		calsob = 75
	elif numerosob == 2:
		calsob = 110
	elif numerosob == 3:
		calsob = 170	
	elif numerosob == 4:
		calsob = 200	
	if numerobeb == 1: 
		cal3 = 20
		print("Entradas:" ,numeroprato, "," ,numerosob,",", numerobeb)
		print("Calorias:", cal+calsob+cal3 , "cal")
	elif numerobeb == 2: 
		cal3 = 70
		print("Entradas:" ,numeroprato, "," ,numerosob,",", numerobeb)
		print("Calorias:", cal+calsob+cal3 , "cal")
	elif numerobeb == 3: 
		cal3 = 100
		print("Entradas:" ,numeroprato, "," ,numerosob,",", numerobeb)
		print("Calorias:", cal+calsob+cal3 , "cal")
	elif numerobeb == 4: 
		cal3 = 65
		print("Entradas:" ,numeroprato, "," ,numerosob,",", numerobeb)
		print("Calorias:", cal+calsob+cal3 , "cal")




	