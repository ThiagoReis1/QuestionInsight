from numpy import*
a=array(eval(input()))
i=0
s=0
while i<size(a):
	if a[i]>200:
		s=s+a[i]*0.15
	i=i+1
s=sum(a)-s
print(round(s,2))
#	Todos os descontos 20, 0, 0 = 20
#s = "" sum(a)-> 233 + 163 + 147 = 700

# sum(a) - s
	