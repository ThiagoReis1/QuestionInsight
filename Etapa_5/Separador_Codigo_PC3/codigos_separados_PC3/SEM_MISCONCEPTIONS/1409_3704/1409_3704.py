Atack = input("espada ou cauda:")
D1 = int(input("D1:"))
D2 = int(input("D2:"))
D3 = int(input("D3:"))
D4 = int(input("D4:"))

EspFla = ( D1 + D2 + D3 + D4 ) + 24

CauConst = ( D1 + D2 + D3 ) * D4

if (Atack == "espada"):
	print(EspFla)

else :
	print(CauConst)
	

