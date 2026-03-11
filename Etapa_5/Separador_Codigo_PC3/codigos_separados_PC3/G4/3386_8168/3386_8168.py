var1=input("radianos ou graus: ").upper()
var2= float(input(""))

if(var1=="G"):
	var3=0.0174533*var2
else:
	var3=var2/0.0174533
print(round(var3,2))