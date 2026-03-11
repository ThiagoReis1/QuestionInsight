a1=input("b ou c: ")
a2=float(input("fatias de: "))
a3=float(input("capp: "))

cp=a3*5.50

if a1=="B":
	b=a2*3.00
	total=b+cp
	print(total)
if a1=="C":
	cr=a2*6.00
	total=cr+cp
	print(total)
