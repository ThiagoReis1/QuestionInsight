a=int(input("pergaminhos: "))
b=int(input("varinhas mágicas: "))
c=int(input("percentual pergaminhos: "))
d=int(input("percentual varinhas: "))

x=0
y=0

while(x<=80000):
	a=a+((c*a)/100)
	b=b+((d*b)/100)
	y=y+a+b
	x=x+1
	
print(x)



	
	