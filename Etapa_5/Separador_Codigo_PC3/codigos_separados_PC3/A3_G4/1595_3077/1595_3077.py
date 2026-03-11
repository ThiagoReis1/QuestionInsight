x = input("string:").upper()
xn =x.replace(" ","")
nv = ""
i = -1
while (i >= -len(xn)):
	nv = nv + xn[i]
	i = i -1
print(xn)
if(xn == nv):
	xk=1
else:
	xk=0
print(2)

