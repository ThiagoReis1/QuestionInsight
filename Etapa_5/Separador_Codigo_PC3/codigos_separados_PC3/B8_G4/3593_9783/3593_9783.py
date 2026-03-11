from numpy import*
fjkfh = array(eval(input(": ")), dtype = int)
gy = 200
z = 0
while z < (len(fjkfh)):
	enel = fjkfh[z]
	if enel == 1 or enel == 3 or enel == 5:
		gy = gy /2
	elif enel == 2 or enel ==4 or enel == 6:
		gy = gy *3
	z = z+ 1
print(gy)
