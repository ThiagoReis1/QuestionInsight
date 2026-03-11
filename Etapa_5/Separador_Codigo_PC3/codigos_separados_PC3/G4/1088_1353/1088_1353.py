n1=float(input("digite valor da nota"))
n2=float(input("digite valor da nota"))
n3=float(input("digite valor da nota"))
n4=float(input("digite valor da nota"))
n5=float(input("digite valor da nota"))

media=(n1+n2+n3+n4+n5)/5
print(round(media,2))

if(media>=7):
	print("Aprovacao")
else:
	print("Reprovacao")
