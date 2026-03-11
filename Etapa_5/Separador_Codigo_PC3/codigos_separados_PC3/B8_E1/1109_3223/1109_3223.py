idade = int(input())
peso = float(input())

print ("Entradas:",idade , "anos e", peso ,"kg")


if ((idade >= 12) and (peso >= 60)):
	 print("Dosagem: 1000 mg")
		
elif ((idade >= 12) and (peso < 60)):
		print ("Dosagem: 875 mg")
	
elif ((idade < 12)):
		if ((peso == 1) or (peso == 2) or (peso ==3) or (peso ==4) or (peso==5)):
		   print ("Dosagem: 75 mg")
	
		elif ((peso == 6) or (peso ==7) or (peso==8) or (peso==9)):
		   print("Dosagem: 125 mg")
		
		elif ((peso == 9) or (peso  ==10) or (peso ==11) or (peso==12) or (peso==13) or (peso==14) or (peso==15)):
		   print("Dosagem: 250 mg")
		
		elif ((peso == 16) or (peso==17) or (peso==17) or (peso==19) or (peso==20) or (peso==21) or (peso==22) or (peso==23) or (peso==24)):
		   print("Dosagem: 375 mg")
		
		elif ((peso == 24) or (peso==25) or (peso==26) or (peso==27) or (peso==28) or (peso==29) or (peso==30)):
		   print("Dosagem: 500 mg")
		
		elif ((peso > 30) or(peso < 500)):
			print("Dosagem: 750 mg")
		
if (((idade <=0) or (idade >= 130)) and ((peso <= 0.0) or (peso >= 550))):
	print("Dados invalidos")