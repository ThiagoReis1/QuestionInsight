a=int(input("quantidade pergaminhos"))
b=int(input("quantidade de varinhas"))
c=int(input("percentual de pergaminhos"))
d=int(input("percentual de varinhas "))
t=0
x=1
while (x<=8000):
	a=a+(c/100)
	b=b+(d/100)
	x=x+a+b
	t= t+30
print(t)
		