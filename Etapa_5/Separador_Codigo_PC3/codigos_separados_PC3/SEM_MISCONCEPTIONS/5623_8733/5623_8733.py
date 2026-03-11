qual = input("B pra bolo e S se quiser salgado, campeao: ")
qt = int(input("quantidade de fatias de bolo ou salgados: "))
qtc = int(input("quantidade de capuccinos meu nobre: "))

presalccino = float((qt * 4) + (qtc * 7.5))
prebolccino = float((qt * 5) + (qtc * 7.5))

if qual == "S":
	print(presalccino)
else:
	print(prebolccino)