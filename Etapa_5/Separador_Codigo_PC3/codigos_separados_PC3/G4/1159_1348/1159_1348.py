a=int(input("peixes a:"))
b=int(input("peixes b:"))
pa=float(input("percentual de a:"))
pb=float(input("percentual de b:"))
m=int(input("maximo do viveiro:"))
y=1
pa+=1
pb+=1
while((a+b)<m):
	a*=pa
	b*=pb
	y+=1
print(y)