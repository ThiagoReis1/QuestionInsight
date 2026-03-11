a = int(input("quantidade de duplas deliciosas: "))

if a > 3:
	v1 = a*32.90
	vt = v1 - (v1*0.20)
	print(round(vt,2))
else:
	vt = a*32.90
	print(round(vt,2))