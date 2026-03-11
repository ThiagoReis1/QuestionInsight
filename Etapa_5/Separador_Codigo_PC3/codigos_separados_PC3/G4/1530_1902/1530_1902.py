a=int(input("quantidade de pergaminho:"))
b=int(input("quantidade de varinhas:"))
pa=float(input("percentual de :"))
pb=float(input("PB:"))

t=0
while(a+b<80000):
	a=a+(a*pa/100)
	b=b+(b*pb/100)
	t=t+1
print(t)