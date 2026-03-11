p1= float(input("p1:"))
p2= float(input("p2:"))
p3= float(input("p3:"))
p4= float(input("p4:"))

m = (p1+p2+p3+p4)/4

if (m>=5.0):
	print (round(m,2))
	print ("Aprovacao")
else:
	print (round(m,2))
	print ("Reprovacao")