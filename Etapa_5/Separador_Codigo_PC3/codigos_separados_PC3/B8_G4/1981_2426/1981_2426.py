c = (input().upper())
vezes = input().upper()
if(c == "CAMPEAO"):
	x = "06-VEZES"
	y = "01-VEZES"
	z = "03-VEZES"
	if(vezes == x):
		print("CORINTHIANS")
	elif(vezes == z):
		z = "3-VEZES"
		print("SANTOS")
elif(c == "VICE CAMPEAO"):
	if(vezes == x):
		x ="6-VEZES"
		print("INTERNACIONAL")
	elif(vezes == y):
		y = "1-VEZ"
		print("FLAMENGO")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")