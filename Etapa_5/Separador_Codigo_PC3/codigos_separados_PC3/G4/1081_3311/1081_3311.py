a=float(input("Digite um numero:"))
b=float(input("Digite um numero:"))
c=float(input("Digite um numero:"))
d=float(input("Digite um numero:"))
media=(a+b+c+d)/4
if(round(media,2)>=5):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")