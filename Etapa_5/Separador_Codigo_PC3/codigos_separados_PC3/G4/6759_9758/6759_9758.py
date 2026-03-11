d = int(input("distancia:"))

if d < 10:
	taxa = 5.5
elif d == 10:
	taxa = 7.75
else:
	taxa = 10
	
print(50+taxa)