a = float(input("qual a nota a: "))
b = float(input("qual a nota b: "))
c = float(input("qual a nota c: "))
d = float(input("qual o valor d:"))
e = float(input("qual o valor e: "))

mda = round((a+b+c+d+e)/5 ,2)
print(mda)
if(mda >= 6.0):
	msg = "Aprovacao"
	print(msg)
else:
	msg = "Reprovacao"
	print(msg)
	
	