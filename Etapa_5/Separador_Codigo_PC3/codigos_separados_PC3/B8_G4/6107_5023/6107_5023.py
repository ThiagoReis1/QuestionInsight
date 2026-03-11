q = float(input("Quantidade comum: "))
if (q>0):
	if (q < 17.5):
		t = q + 1.5
	elif (17.5<=q and q<35 ):
		t = q + 2.3
	elif (35<=q  and q<50):
		t = q + 3.3
	elif (q > 50):
		t = q + 4.7
	print(round(t,1))
