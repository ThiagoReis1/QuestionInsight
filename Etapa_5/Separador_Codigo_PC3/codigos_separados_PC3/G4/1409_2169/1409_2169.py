att = input("digite o tipo de ataque : ")

D1 = int(input("digite o valor de D1 : "))
D2 = int(input("digite o valor de D2 : "))
D3 = int(input("digite o valor de D3 : "))
D4 = int(input("digite o valor de D4 : "))

if ( att.upper() == espada ) :
	print((D1 + 6) + (D2 + 6) + (D3 + 6) + (D4 + 6))
if (att.upper() == cauda ) :
	print((D1  + D2 + D3)*D4)