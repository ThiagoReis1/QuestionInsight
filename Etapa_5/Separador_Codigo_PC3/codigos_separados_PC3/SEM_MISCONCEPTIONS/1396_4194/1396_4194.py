vl_c = float(input("Valor consumido: "))

if(vl_c <= 300):
	gorjeta = (vl_c / 100) * 10
else:
	gorjeta = (vl_c / 100) * 6
	
print(round( vl_c + gorjeta , 2))