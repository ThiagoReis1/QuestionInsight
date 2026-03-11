comb =  int(input("quanto de combustivel"))

if (comb < 17.5):
	t = comb + 0.8
	print(t)
	
elif (17.5 <= comb < 35.0):
	t = comb + 1.3
	print(t)
	
elif (35.5<= comb <50.0 ):
	t = comb + 2.1
	print(t)
	
else:
	t = comb + 3.0
	print(t)
	