x=int(input("valor de x:"))
y=int(input("valor de y"))

acl=0

while (x<=y):
	if (x%3==0):
		acl=acl+x
	x=x+1
print(acl)