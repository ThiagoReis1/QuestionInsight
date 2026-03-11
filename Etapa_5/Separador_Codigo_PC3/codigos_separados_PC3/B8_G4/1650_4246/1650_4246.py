st = str(input("Insira a string: ")).lower().split(',')

p = 0
c = 0
r = 0
l = 0
b = 0


if(st == "P"):
	p = p + 1
elif(st == "C"):
	c = c + 1
elif(st == "R"):
	r = r + 1
elif(st == "L"):
	l = l + 1
elif(st == "B"):
	b = b + 1

print(p)