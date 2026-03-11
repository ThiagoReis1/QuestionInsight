s=input("String:")
b=len(s)
a=0
e=0
ee=0
o=0
u=0
for i in range(b):
	if s[i]=="a":
		a=a+1
	elif s[i]=="e":
		e=e+1
	elif s[i]=="i":
		ee=ee+1
	elif s[i]=="o":
		o=o+1
	elif s[i]=="u":
		u=u+1
print("a:",a)
print("e:",e)
print("i:",ee)
print("o:",o)
print("u:",u)
