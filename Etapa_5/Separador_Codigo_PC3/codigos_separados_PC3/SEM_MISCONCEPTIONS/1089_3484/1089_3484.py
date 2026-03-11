c1=float(input())
c2=float(input())
c3=float(input())
limite=float(input())
total=c1+c2+c3
print(round(total,2))
if total <= limite:
	print("Nao ultrapassou")
else:
	print("Ultrapassou")
