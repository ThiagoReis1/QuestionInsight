var1 = float(input("horas trabalhadas:"))
if var1<= 20 :
	x = var1 * 50
else :
	x = (20 * 50) + 70 * (var1 - 20)
print(round(x,2))