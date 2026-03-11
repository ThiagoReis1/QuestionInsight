n1 = float(input("nota1:"))
n2 = float(input("nota2:"))
n3 = float(input("nota3:"))
n4 = float(input("nota4:"))

media = round((n1+n2+n3+n4)/4,2)

print(media)

if(media>=5):
	print("Aprovacao")
else:
	print("Reprovacao")
