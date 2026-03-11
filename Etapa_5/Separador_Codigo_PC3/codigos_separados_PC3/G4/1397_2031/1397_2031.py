asf = float(input("Area a ser fertilizada :"))

if(asf <= 10**4):
	vm = asf * 5
	print (float(round(vm , 2)))	
else:
	vr = (asf - (10 ** 4)) * 4
	vm = 10**4 * 5 + vr
	print (float(round(vm , 2)))
