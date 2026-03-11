var1 = float(input("Peso da encomenda:"))
if (var1<=5000):
	print(round(0.05*var1, 2))
else:
	print(round(0.04*var1+60, 2))