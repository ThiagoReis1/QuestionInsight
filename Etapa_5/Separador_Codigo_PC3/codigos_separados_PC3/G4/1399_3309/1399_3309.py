ar = int(input("votos Ambrosio: "))
do = int(input("votos Demelza: "))
x = ar/(ar + do)*100
y = do/(do+ar)*100
if ar > do:
	print("Ambrosio Rutra")
	print(round(x,2))
else:
	print("Demelza Olecram")
	print(round(y,2))
	