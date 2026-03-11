d = int(input("insira um numero: "))
if d <7:
	taxa = 15
elif d == 7:
	taxa = 12
elif d> 7:
	taxa = 10
	
total = (100*d)+taxa
print(round(total,2))
	