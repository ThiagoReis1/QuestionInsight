vx = float(input(": "))

if(vx>=-100 and vx<0):
	print(round((-(1/vx)), 4))

elif(vx>0 and vx<=100):
	print(round((1/vx), 4))

else:
	print("entrada invalida")