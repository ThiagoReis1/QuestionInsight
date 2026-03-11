x = input(int("Qual a velocidade do trem:")
y = input(int("Quanto tempo de viagem: "))

d = velocidade * tempo

print("Entrada: " ,x , "km/h e" ,y ,"h" ) 
if(d >= 1400 or x <= 0):
	print()
elif(d == 100):
	print("Proxima parada:Bravos " )
elif(d == 200):
	print("Proxima parada:Castamere" )
elif(d == 400):
	print("Proxima parada:Doriath" )
elif(d == 600):
	print("Proxima parada:Edoras" )
elif(d == 750):
	print("Proxima parada:Fangorn" )
elif(d == 1150):
	print("Proxima parada:Gondor" )
elif(d == 1400):
	print("Proxima parada:Hogsmead" )
else:
	print("Dados invalidos")