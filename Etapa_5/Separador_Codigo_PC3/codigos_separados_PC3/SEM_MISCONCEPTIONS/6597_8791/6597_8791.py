num=int(input())
cont=
a=0
b=0
c=0

while cont<num:
	cont+=1
	esc = input("").upper()
	if esc == "A":
		a=a+1
	elif esc == "B":
		b=b+1
	elif esc == "C":
		c=c+1
print("A=", a)
print("B=", b)
print("C=",  c)