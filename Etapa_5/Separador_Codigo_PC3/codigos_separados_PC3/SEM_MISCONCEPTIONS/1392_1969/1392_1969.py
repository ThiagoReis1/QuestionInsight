consumo = int(input("m³ de agua consumido: "))

agua1 = consumo * 3.00 + 30.00
agua2 = consumo * 3.50 + 30.00

if(consumo == "agua1") :
	print(round(agua1, 2))

else:
	print(round(agua2, 2))