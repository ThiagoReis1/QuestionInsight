a = input("digite ")
q = int(input("quantidade "))
qa = int(input("quantidade de a "))

tapioca = 4.50
salgado = 5.00
acai = 12.00

if "S" == a.upper():
	g = q * salgado + qa * acai
	print(round(g,1))
else:
	g = q * tapioca + qa * acai
	print(round(g,1))