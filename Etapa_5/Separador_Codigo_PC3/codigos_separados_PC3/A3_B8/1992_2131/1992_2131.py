a = input().lower()
if(a!="glutamina" and a!="histidina" and a!="prolina"):
	print("Entrada:",a)
	print("Dado Invalido")

glutamina = (5*12.011+8*1.00794+1*14.00674+4*15.999)
histidina = (6*12.011+10*1.00794+3*14.00674+2*15.999)
prolina = (5*12.011+10*1.00794+14.00674+2*15.999)

if(a=="glutamina"):
	print(round(5*12.011+8*1.00794+1*14.00674+4*15.999,2))
elif(a=="histidina"):
	print(round(6*12.011+10*1.00794+3*14.00674+2*15.999,2))
elif(a=="prolina"):
	print(round(5*12.011+10*1.00794+14.00674+2*15.999,2))


	
	




