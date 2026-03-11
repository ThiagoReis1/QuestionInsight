from numpy import*

x=input("x: ")
y=""

if len(x)>11 or len(x)<11:
	print("INVALIDO")

else:
	for i in range(len(x)):
		if(i%2!=0):
			y=y+x[i]
print(y)