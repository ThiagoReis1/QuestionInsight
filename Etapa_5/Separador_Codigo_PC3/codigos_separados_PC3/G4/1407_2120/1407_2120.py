#start!
qpi = int(input("Pontos de vida:"))
Da = int(input("Sorteio 1:"))
Db = int(input("Sorteio 2:"))
Dc = int(input("Sorteio 3:"))

N = 10*(Da+Db+Dc)

if ((qpi-N) > 0):
	print (qpi- N)
	print ("VIVO")
else:
	print ("0")
	print("MORTO")