#victor do vale moreira
#21/07/16

x = float(input("valor da velocidade do trem"))
y = float(input("tempo de viagem"))
if(x <= 0 ) or (y < 0):
	print()



s = x * y
if(s < 100):
	print("Bravos")
elif(s >= 100) and (s <=200):
	print("Castamare")
elif(s >= 200) and (s <= 400):
	print("Doriath")
elif(s >= 400) and (s <= 600):
	print("Edoras")
elif( s >= 600) and (s <= 750):	
	print("Fangorn")
elif(s > 750) and (s <= 1150):
	print("Gondor")
elif( s > 1400):
	print("Hogsmead")
else:
	print("Entrada invalida")