a = input("P ou T: ")
b = int(input("tortas ou pastel: "))
c = int(input("cappuccino: "))

if a == "T" :
	d = (b*6)+(c*4.50)
	print(d)
else:
	d = (b*5)+(c*4.50)
	print(d)
	