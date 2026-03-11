me=input("medida:")
v=float(input("valor:"))
if(me=="K"):
	k=35.274*v
else:
	k=v/35.274
print(round(k,2))