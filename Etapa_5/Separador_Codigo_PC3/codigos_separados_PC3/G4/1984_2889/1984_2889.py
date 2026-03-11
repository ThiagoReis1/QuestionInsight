
r = input ("Resultado do time na competição: ").upper()
q = (input ("Quantas vezes o time alcançou esse resultado?")).upper()

if ( r == "CAMPEAO") and (q == "11-VEZES"): 
	t = "REAL MADRID"
	print (t)
elif ( r == "CAMPEAO") and (q == "05-VEZES" or q == "5-VEZES"): 
	t = "BARCELONA" 
	print (t)
elif(r == "VICE-CAMPEAO") and (q == "01-VEZ" or q == "1-VEZ"):
	t = "CHELSEA"
	print (t)
elif (r == "VICE-CAMPEAO") and (q == "04-VEZES" or q == "4-VEZES"):
	t = "MILAN"
	print (t)
else: 
	print ("TIME DE FUTEBOL NAO IDENTIFICADO.")