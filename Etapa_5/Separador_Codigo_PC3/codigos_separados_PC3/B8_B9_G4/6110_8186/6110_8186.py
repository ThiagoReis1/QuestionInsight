c = int(input("Diga o valor: "))

if (c < 17.5):
	x = c + 10.5
	print(round(x, 1))
	
elif (c >= 17.5) and (c < 35):
	y = c + 14
	print(round(y, 1))

elif (c >= 35) and (c < 50):
	z = c + 18.6
	print(round(z, 1))
	
elif (c >= 50):
	w = c + 24.5
	print(round(w, 1))