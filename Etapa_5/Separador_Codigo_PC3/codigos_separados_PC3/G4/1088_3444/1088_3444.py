n1 = float(input("informe a nota"))
n2 = float(input("informe a  nota"))
n3 = float(input("informe a nota"))
n4 = float(input("informe a nota"))
n5 = float(input("informe a nota"))

media = (n1 + n2 + n3 + n4 + n5)/5 
print(round(media,2))

if (media >= 7.0):
	print("Aprovacao")
else:
	print("Reprovacao por nota")
	
