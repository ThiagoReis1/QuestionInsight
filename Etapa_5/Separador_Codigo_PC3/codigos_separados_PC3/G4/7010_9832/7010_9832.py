x = input("X: ")
y = input("Y: ")

try :
	x = int(x)
	y = int(y)
	
except ValueError :
	print("Bah")
	
else :
	while ( x <= y ) :
		print(x)
		x += 7