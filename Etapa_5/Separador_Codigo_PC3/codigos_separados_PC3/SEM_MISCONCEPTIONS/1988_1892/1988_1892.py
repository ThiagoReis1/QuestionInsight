nome =input("Nome do aminoacido: ")


if(nome == "ARGININA"):
   total = (12.011 * 6)+ (1.00794 * 15) + (14.00674 * 4) + (15.9994 * 2)
   print(round(total,2))
elif(nome == "TIROSINA"):
	total = (12.011 * 9) + (1.00794 * 11) + (14.00674 * 1) +(15.9994 * 3)
	print(round(total,2))

elif(nome == "TRIPTOFANO"):
	total = (12.011 * 11) + (1.00794 * 11) + (14.00674 * 2) + (15.9994 *2)
	print(round(total,2))

else:
	print("Entrada:",nome)
	print("Dado Invalido")
	
	