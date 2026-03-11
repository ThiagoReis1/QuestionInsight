x = int(input("Tempo de voo:"))

if (x <= 200):
	print (5000 + (100*x))
elif (x > 200):
	print (8000+ (100*200)+ (90*(x-200)))