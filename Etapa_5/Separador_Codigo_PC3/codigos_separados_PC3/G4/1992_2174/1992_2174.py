n = input("digite o aminoacido (glutamina, histidina ou prolina): ")

if(n.lower()  == "glutamina"):
	x = (12.011*5) + (1.00794*8) + 14.00674 +(15.999*4)
	print(round(x, 2))
elif(n.lower()  == "histidina"):
	x = (12.011*6) + (1.00794*10) + (14.00674*3) + (15.999*2)
	print(round(x, 2))
elif(n.lower()  == "prolina"):
	x = (12.011*5) + (1.00794*10) + (14.00674) + (15.999*2)
	print(roun(x, 2))
else: 
	print("Entrada:", n.lower())
	print("Dado Invalido")