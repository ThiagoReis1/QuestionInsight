qii=int(input("qi de g infantaria: "))
qic=int(input("qi de g cavalaria: "))
pi=float(input("percentual: "))/100
pc=float(input("percentual: "))/100

a=qii
b=qic
c=pi
d=pc
soma=0
i=0
while(a+b<50000):
	a=a+(a*c)
	b=b+(b*d)
	soma=soma+(a+b)
	i=i+1

print(i)
	