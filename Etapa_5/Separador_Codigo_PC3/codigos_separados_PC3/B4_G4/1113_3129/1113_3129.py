x = (float(input("insira uma idade:")))
y= (float(input("insira um peso:")))

if(x <= 20) and (y <= 60):
	print("Grupo 9")
elif(x>20) or (x<50) and (y>60) or (y<90):
	print("Grupo 5")
elif(x>50) and (y>90):
	print("Grupo 1")
elif(x<=20) and (y>60) or (y<90):
	print("Grupo 8")
elif(x<=20) and (y>90):
   print("Grupo 7")
elif(x>20) or (x<50) and (y<=60):
   print("Grupo 6")
elif(x>20) or (x<50) and (y>90):
   print("Grupo 4")
elif(x>50) and (y<=60):
   print("Grupo 5")
elif(x>50) and (y>60) or (y<90):
	print("Grupo 2")
else:
	("Entrada",x,y,"invalida")
	

		  