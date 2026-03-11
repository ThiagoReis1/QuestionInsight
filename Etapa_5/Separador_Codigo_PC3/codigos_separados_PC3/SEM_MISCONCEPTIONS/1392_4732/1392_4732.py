var1 = float(input())
taxa = 30
tarifa1 = 3
tarifa2 = 3.5
if(var1 < 10):
	print(round(taxa+tarifa1*var1,2))
if(var1 >= 10):
	print(round(taxa+tarifa2*var1,2))
