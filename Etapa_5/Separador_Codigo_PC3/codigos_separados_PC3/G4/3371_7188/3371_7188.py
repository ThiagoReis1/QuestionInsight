me= input("medida em K ou M")
vm= float(input("valor da medida"))
if me== "K":
	m = vm/1.60934
	print(round(m,2))
	
else:
	k= 1.60934 * vm  
	print(round(k,2))