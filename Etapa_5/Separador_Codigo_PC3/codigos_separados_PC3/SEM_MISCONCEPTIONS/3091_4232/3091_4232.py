letra=input("Resultado: V, E ou D? ")
pont=0
t=1v
v

while(letra != "X"):
	if(letra.upper()=="V"):
		pont=pont+3
	elif(letra.upper()=="E"):
		pont=pont+1
	elif(letra.upper()=="D"):
		pont=pont+0
	else:
		pont=pont+0
	print(pont)
	t=t+1
	letra=input("Resultado: V, E ou D? ")
print(round((pont/t)*100, 2))