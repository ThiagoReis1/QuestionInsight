w=("as ruinas de petra").upper()
x=("taj mahal").upper()
y=("machu picchu").upper()
z=("cristo redentor").upper()
a=("informacao nao identificada").upper()

C = input("Continente: ")
P = input("Pais: ")
if ((C=="Asia") and (P=="Jordania") or (P=="India")):
	if (P=="Jordania") and (P=="India"):
		if (P=="Jordania"):
			print (w)
		elif(P=="India"):
			print (x)
if((C=="America-do-Sul") and (P=="Peru") or (P=="Brasil")):
	if(P=="Peru"):
		print (y)
	elif(P=="Brasil"):
		print (z)
else:
	print(a)
