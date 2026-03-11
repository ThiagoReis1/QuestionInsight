aminoacido = input("digite aminoacido: ")


oxigenio =  15.9994
carbono = 12.011
nitrogenio = 14.0067
enxofre = 32.066
hidrogenio = 1.00794

calculo1 = carbono * 6 + hidrogenio * 13 + nitrogenio * 1 + oxigenio * 2
calculo2 = carbono * 5 + hidrogenio * 11 + nitrogenio * 1 + oxigenio * 2 + enxofre * 1 

if	(aminoacido.lower() == "isoleucina"):
	print(round(calculo1, 2))

else:
	print(round(calculo2, 2))
	