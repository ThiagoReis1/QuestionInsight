a = input("t/p").upper()
b = int(input("quantidade de tortas ou pastel? "))
c = int(input("quantos c "))

if a=="T":
	x = b*6.00
	y = c*4.50
	z = x+y
	print(z)

else:
	l = b*5.00
	k = c*4.50
	j = l+k
	print(j)