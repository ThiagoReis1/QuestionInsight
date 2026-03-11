comb = float(input())

if(comb<17.5):
	c = comb + 0.8
	print(round(c, 1))
elif(17.5<=comb<35):
	c = comb + 1.3
	print(round(c, 1))
elif(35<=comb<50):
	c = comb + 2.1
	print(round(c, 1))
else:
	c = comb+3
	print(round(c, 1))