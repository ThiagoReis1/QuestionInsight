n1 = float(input("digite o valor da primeira nota: "))
n2 = float(input("digite o valor da segunda nota: "))
n3 = float(input("digite o valor da terceira nota:"))
n4 = float(input("digite o valor da quarta nota: "))
n5 = float(input("digite o valor da quinta nota: "))

media_arit = (n1+n2+n3+n4+n5)/5

if(media_arit >= 7.0):
	print(round(media_arit , 2))
	print("Aprovacao")
else:
	print(round(media_arit , 2))
	print("Reprovacao por nota")