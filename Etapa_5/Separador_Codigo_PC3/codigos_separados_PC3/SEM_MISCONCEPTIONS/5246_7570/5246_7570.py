x = float(input("Idade: "))
y = float(input("Peso: "))
if(x<20):
elif(y<60):
	g=9
	print("Grupo de risco ", g)
elif(y<60 and y<90):
	g=8
	print("Grupo de risco ", g)
elif(y>90):
	g=7
	print("Grupo de risco ", g)
	
if(x>20 and x<50):
elif(y<60):	
	g=6
	print("Grupo de risco ", g)
elif(y>60 and y<90):
	g=5
	print("Grupo de risco: ", g)
elif(y>90):
	g=4
	print("Grupo de risco: ", g)
if(x>50):
elif(y>50):
	g=3
	print("Grupo de risco: ", g)
elif(y>60 and y<90):
	g=2
	print("Grupo de risco: ", g)
elif(y>90):
	g=1
	print("Grupo de risco: ", g)
else:
	print("Dados invalidos")