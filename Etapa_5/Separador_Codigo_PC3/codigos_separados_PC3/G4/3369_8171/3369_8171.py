unid=input("").upper()
v=float(input(""))

if unid=="M":
	v*=3.6
if unid=="K":
	v/=3.6
	
print(round(v,2))