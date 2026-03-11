x=float(input("valor 1:"))
y=float(input("valor 2:"))
z=float(input("valor 3:"))
media=(x+y+z)/3
if(media>=6):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")
