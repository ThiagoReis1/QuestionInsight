x = int (input("valor do numero "))
a = x//10000
b = x%10000//100
c = x%100
if( x == (a*a*a) + (b*b*b) + (c*c*c)):
	print ("X atende a propriedade")
else:
	print ((a*a*a)+(b*b*b)+(c*c*c))