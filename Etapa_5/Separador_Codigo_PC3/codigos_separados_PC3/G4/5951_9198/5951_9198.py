x = input("T ou S: ")
Y = int(input("Quantidade de ta ou sa: "))
z = int(input("Quantidade de acai: "))

ta = 4.50
sa = 5.00
ac = 12.00

if x == "T":
	vl =  (Y*ta) + (z*ac)
	print(vl)
else:
	vl = (Y*sa) + (z*ac)
	print(vl)