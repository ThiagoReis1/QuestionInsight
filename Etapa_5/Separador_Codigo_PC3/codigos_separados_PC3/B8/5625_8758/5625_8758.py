ts = input("digite a quntidade para t ou s: ")

if(ts == "T"):
	tapioca = int(input("quantidade de tapiocas: "))
	acai = int(input("quantidade de acai: "))
	total = (10.00 * acai) + (5.50 * tapioca)
	
elif(ts == "S"):
	salgado = int(input("quantidade de salgados: "))
	acai = int(input("quatidade de acai: "))
	total = (10.00 * acai) + (4.00 * salgado)
	
print(total)


	
	