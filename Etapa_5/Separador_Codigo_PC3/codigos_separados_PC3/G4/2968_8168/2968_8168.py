var1= input("s ou l: ").upper()
var2= int(input(""))
var3=int(input(""))


lan= 5
sal= 3.5
refri= 4

if(var1=="L"):
	vt=var2*lan+var3*refri
else:
	vt=var2*sal+var3*refri
print(round(vt,2))
	
	