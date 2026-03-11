c=float(input("valor consumido: "))
v=c
a=v+(v*10)/100
b=v+(v*6)/100
if(v<=300):
	print(round(a, 2))
else:
	print(round(b, 2))	
	
if(p<=150):
	print(a)
else:
	print(b)
