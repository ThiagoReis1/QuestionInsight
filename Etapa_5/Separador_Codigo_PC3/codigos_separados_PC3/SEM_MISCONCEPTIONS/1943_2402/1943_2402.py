aminoacido = input()

oxigenio = 15.9994
carbono = 12.011
nitrogenio = 14.0067
enxofre = 32.066
hidrogenio = 1.00794

if (aminoacido == "isoleucina"):
	isoleucina = (6*carbono) + (13*hidrogenio) + nitrogenio + (2*oxigenio)
	print(round(isoleucina, 2))
			
if (aminoacido == "metionina"):
	metionina = (5*carbono) + (11*hidrogenio) + nitrogenio + (2*oxigenio) + enxofre
	print (round(metionina, 2))