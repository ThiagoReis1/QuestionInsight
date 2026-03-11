nota=float(input("Digite a sua nota:  "))
if nota>=9 and nota<=10:
	print("A")
elif nota>=8:
	print("B")
elif nota>=7:
	print("C")
elif nota>=6:
	print("D")
elif nota>=4:
	print("E")
elif nota<4 and nota>=0:
	print("F")
else:
	print("ERRO")