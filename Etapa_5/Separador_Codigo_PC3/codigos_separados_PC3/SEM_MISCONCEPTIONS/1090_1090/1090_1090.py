a = float(input())
b = float(input())
c = float(input())
d = float(input())
limite = float(input())

total = a+b+c+d

if( total <= limite):
	print(round(total,2))
	print("Sim")
else:
	print(round(total,2))
	print("Nao")