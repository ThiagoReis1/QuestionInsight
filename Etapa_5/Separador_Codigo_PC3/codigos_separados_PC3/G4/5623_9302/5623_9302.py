b_ou_s = input("b ou s: ")
bolos_ou_salgados = int(input("bolo ou salgado: "))
capp = int(input("capp: "))

p1 = 5.00
p2 = 4.00
p3 = 7.50

B = (bolos_ou_salgados * p1) + (capp * p3)
S = (bolos_ou_salgados * p2) + (capp * p3)

if b_ou_s == "B" :
	print(B)
	
else:
	b_ou_s == "S"
	print(S)

