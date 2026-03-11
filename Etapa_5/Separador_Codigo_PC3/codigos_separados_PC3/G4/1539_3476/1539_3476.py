x = float(input())
k = int(input())
cont=1
s = 1
while(cont<=k):
	s = s + ((-1)**cont)*(x**cont)
	cont=cont+1
print(round(cont,7))
	