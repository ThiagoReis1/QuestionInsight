cc = int(input("Quantidade de combustivel comum: "))
w = 0
if cc > 0:
	if cc < 17.5:
		w = 1.5 + cc
	elif 17.5 < cc < 35:
		w = 2.3 + cc
	elif 35 < cc < 50:
		w = cc + 3.3
	else:
		w = cc + 4.7
	print(round(w, 1))