unid = input("Qual unidade a medida esta? (L/K) ")
var = float(input("Qual o valor medida? "))

if (unid == "K"):
	cal1 = 2.20462*var
	print(round(cal1,2))
else:
	cal2 = var/2.20462
	print(round(cal2,2))