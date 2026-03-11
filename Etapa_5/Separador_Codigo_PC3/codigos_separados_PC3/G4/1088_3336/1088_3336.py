n1 =float(input("qual a nota"))
n2 =float(input("qual a nota")) 
n3 =float(input("qual a nota"))
n4 =float(input("qual a nota"))
n5 =float(input("qual a nota"))
ma =(n1+n2+n3+n4+n5)/5
print(round(ma,2))
if(ma >= 7):
	print("Aprovacao")
else:
	print("Reprovacao por nota")