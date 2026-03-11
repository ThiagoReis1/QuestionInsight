m = input("S ou N")
p = float(input(""))
a = float(input(""))
k = 0.8
formula = (p*a)*k
if (m == 'S'):
	print(round(formula,2))
else:
	print(round(p*a,2))