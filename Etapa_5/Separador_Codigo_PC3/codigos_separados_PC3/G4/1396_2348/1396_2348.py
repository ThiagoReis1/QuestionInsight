vc=float(input("valor consumido:"))
if(vc<=300):
	x=vc+((vc*10)/100)
else:
	x=vc+((vc*6)/100)
print(round(x,2))