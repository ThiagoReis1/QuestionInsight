peso = float(input("digite o peso da caga:"))
distancia = float(input("digite a distancia percorrida:"))
cod = input("digite o codigo:")

if(cod == "1"):
	icms = 17.0
	total = ((peso * 25) + (distancia * 0.10)) * (1.0 + icms / 100)
	print(round(total,2))

elif(cod == "2"):
	icms = 17.5
	total = ((peso * 25) + (distancia * 0.10)) * (1.0 + icms / 100)
	print(round(total,2))

elif(cod == "3"):
	icms = 18.0
	total = ((peso * 25) + (distancia * 0.10)) * (1.0 + icms / 100)
	print(round(total,2))
	
elif(cod == "4"):
	icms = 20.0
	total = ((peso * 25) + (distancia * 0.10)) * (1.0 + icms / 100)
	print(round(total,2))
	
