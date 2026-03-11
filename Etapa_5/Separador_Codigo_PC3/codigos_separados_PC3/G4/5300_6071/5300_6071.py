v =int(input(""))
t = 0
while(v == 50):
	if(v >= 50):
		t = t + 60
		v = v - (v * 0,25)
	print(round(v, 8))
