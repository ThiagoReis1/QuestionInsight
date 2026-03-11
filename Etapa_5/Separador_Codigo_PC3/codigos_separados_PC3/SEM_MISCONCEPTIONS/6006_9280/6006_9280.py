batata = int(input("quantidade de batata: "))
batatanormal = batata * 0.90
batataatacado = batata * 0.75
if batata < 10 :
	print(round(batatanormal, 2))
else :
	print(round(batataatacado, 2))