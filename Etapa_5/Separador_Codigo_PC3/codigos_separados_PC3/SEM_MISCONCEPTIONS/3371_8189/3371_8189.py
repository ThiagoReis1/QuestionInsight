u=input("(K/M): ")
var=float(input("valor da medida: "))
if(u.upper() == "M"):
	Conta=1.60934*var
else:
	Conta=var/1.60934
	
print(round(Conta,2))