nota = float(input())

if nota<=10 and nota>=0:
	if nota >= 9:
		print("A")
	elif nota >= 8:
		print("B")
	elif nota >= 7:
		print("C")
	elif nota >= 6:
		print("D")
	elif nota >=5:
		print("E")
	else:
		print("F")
else: 
	print("ERRO")