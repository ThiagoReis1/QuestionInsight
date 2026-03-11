pl=input("digite 1 ou 2: ").upper
qp=int(input("digite quantidade: "))
qr=int(input("digite quantidade de refris: "))

lanche=6.00
pizza=4.50
refrigerante=3.00*qr

if(pl =< 1):
	print(pizza*qp+refrigerante)
else:
	print(lanche*qp+refrigerante)