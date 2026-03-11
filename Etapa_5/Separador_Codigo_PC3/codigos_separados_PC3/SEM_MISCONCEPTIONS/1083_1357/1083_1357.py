n1=float(input("Nota=1:"))
nu2=float(input("Nota=2:"))
nu3=float(input("Nota=3:"))

media=(n1+n2+n3)/3

if(media>=6):
   print (round(media,1))
	print ("Aprovacao")

else:
	print (round(media,1))
	print ("Reprovacao")
