O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
pm = 

if (pm == 3*C + 7*H + N + 2*O):
	print("Alanina".upper())
elif (pm == 5*C + 11*H + N + 2*C):
	print("Valina".upper())
elif(pm == 9*C + 11*H + N + 3*O):
	print("Tirosina".upper())
else:
	print("Dado invalido")