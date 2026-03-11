p = float(input("Peso: "))
d = float(input("Distancia: "))
z = int(input("Codigo: "))
cp = 25
cd = 0.1
m = [17,17.5,18,20]
if z==1:
	print(round((p*cp+d*cd)*(1+m[0]/100),2))
elif z==2:
	print(round((p*cp + d*cd)*(1 + m[1]/100),2))
elif z ==3:
	print(round((p*cp+d*cd)*(1+m[2]/100),2))
elif z==4:
	print(round((p*cp+d*cd)*(1+m[3]/100),2))
else:
	print("Codigo invalido")
	


