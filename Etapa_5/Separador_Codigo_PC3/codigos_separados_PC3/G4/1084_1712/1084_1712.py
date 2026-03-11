n1=float(input("qual valor da n1: "))
n2=float(input("qual valor da n2: "))
n3=float(input("qual valor da n3: "))
n4=float(input("qual valor da n4: "))
n=(n1+n2+n3+n4)/4
print(round(n, 1))
if(n>=6):
	print("Aprovado")
else:
	print("Reprovado")