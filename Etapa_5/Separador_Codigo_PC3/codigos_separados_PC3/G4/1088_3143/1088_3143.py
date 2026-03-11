n1 = float(input("n1:"))
n2 = float(input("n2:"))
n3 = float(input("n3:"))
n4 = float(input("n4:"))
n5 = float(input("n5:"))

m =( n1 + n2 + n3 + n4 + n5) / 5
print(float(round(m, 2)))
if (m >= 7):
	msg = "Aprovacao"
	
else:
	msg = "Reprovacao por nota"


print(msg)