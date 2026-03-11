n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

ma = (n1 + n2 + n3 + n4) / 4
   
print(round(ma,2))

if ( ma >= 5.0 ):
	print ("Aprovacao")
else:
	print ("Reprovacao")
