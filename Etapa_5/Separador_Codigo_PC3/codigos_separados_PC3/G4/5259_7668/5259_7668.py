x=float(input(""))
y=int(input(""))
if(y==1):
	z=x*y*0.9
	print(round(z,2))
elif(y==2):
	z=x*y*0.7
	print(round(z,2))
elif(y>=3):
	z=x*y*0.6
	print(round(z,2))
else:
	print("Dados invalidos")