var1 = float(input("Tempo de voo :"))

if var1 <= 200 :
	x = 5000 + var1 * 100
if var1 > 200 :
	x = 8000 + 20000 + (var1-200)*90
print(round(x,2))