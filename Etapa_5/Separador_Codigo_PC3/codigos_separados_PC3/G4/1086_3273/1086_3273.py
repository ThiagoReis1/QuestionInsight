p1 = float(input())
p2 = float(input())
p3 = float(input())

m = (p1 + p2 + p3) / 3
p = round(m, 1)
if(m >= 7.0):
	print(p, "Aprovado")
else: 
	print(p, "Reprovado")