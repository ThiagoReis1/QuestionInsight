from numpy import*
x=array(input("palavras: "))
y=input("palavras: ")
i=0
d=0
yn=""
while(i<len(y)):
	if(y[i]=="R"):
		yn=y.replace("R","L")
	i=i+1
print(yn)
print(size(x))

