conti = input("qual o continente:")
pais = input("qual  o pais:")
if ((conti == "Asia") and (pais == "Jordania")):
	print("as ruinas de petra".upper())
elif ((conti == "Asia") and (pais == "India")):
	print("taj mahal".upper())
elif ((conti == "America-do-Sul") and (pais == "Peru")):
	print("machu picchu".upper())
elif ((conti == "America-do-Sul") and (pais == "Brasil")):
	print("cristo redentor".upper())
else:
	print("informacao nao identificada".upper())