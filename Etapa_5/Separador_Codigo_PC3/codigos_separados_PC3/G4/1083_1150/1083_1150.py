nt1=(float(input("primeira nota= ")))
nt2=(float(input("segunda nota= ")))
nt3=(float(input("terceira nota= ")))
soma=round(nt1+nt2+nt3,2)
media=round(soma/3,2)
print(round(media,2))
if(media>=6):
	print("Aprovacao")
else:
	print("Reprovacao")