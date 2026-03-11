h = (input().lower())

if(h == "histidina"):
	p1 = ((6*12.011)+(10*1.0079)+(3*14.00674)+(2*15.9994))
	print(round(p1, 2))
elif(h == "leucina"):
	p2 = ((6*12.011)+(13*1.0079)+(14.00674)+(2*15.9994))
	print(round(p2, 2))
elif(h == "lisina"):
	p3 = ((6*12.011)+(15*1.0079)+(2*14.00674)+(2*15.9994))
	print(round(p3, 2))
else:
	print("Entrada:", h)
	print("Dado Invalido")