v1= float(input())
v2= float(input())
v3= float(input())
limite= float(input())

total= v1+v2+v3
print(round(total,2))

if(total<=limite):
	print("Nao ultrapassou")
else:
	print("Ultrapassou")