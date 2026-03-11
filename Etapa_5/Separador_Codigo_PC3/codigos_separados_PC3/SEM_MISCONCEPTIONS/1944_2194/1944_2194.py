molecula = input(" ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
leucina = C*6 + H*13 + N + O*2
lisina = C*6 + H*15 + N*2 + O*2
if (molecula == "leucina"):
	print(round(leucina, 2))
else:
	print(round(lisina, 2))
