n1=float(input("Informe o n1:"))
n2=float(input("Informe o n2:"))
n3=float(input("Informe o n3:"))
n4=float(input("Informe o n4:"))

media = (n1 + n2 + n3 + n4 ) / 4
print(round(media,2))
if (media >=5.0):
	print("Aprovacao")
else:
	print("Reprovacao")