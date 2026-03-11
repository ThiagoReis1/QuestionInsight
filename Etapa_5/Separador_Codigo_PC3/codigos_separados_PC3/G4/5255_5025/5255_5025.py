p = float(input("Peso do produto:"))
x = float(input("Distancia:"))
c = int(input("Codigo do estado:"))

cp = 25
cx = 0.10

if c == 1:
	icms = 17
	serv = (p*cp + x*cx)*(1+(icms/100))
	print(round(serv,2))
elif c == 2:
	icms = 17.5
	serv = (p*cp +x*cx)*(1+(icms/100))
	print(round(serv,2))
elif c == 3:
	icms = 18
	serv = (p*cp + x*cx)*(1+(icms/100))
	print(round(serv,2))
else:
	icms = 20
	serv = (p*cp + x*cx)*(1+(icms/100))
	print(round(serv,2))