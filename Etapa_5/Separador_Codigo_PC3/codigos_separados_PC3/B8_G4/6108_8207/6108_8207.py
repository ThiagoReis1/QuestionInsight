l= int(input("Litros: "))
if l>0 and l <17.5:
	l= l+ 1.5
	print(round(l, 1))
	
elif l >= 17.5 and l<35.0:
	l = l + 2.3
	print(round(l, 1))
	
elif l >=35.0 and l < 50.0:
	l= l + 3.3
	print(round(l, 1))
	
elif l > 50.0:
	l = l + 4.7
	print(round(l, 1))

	