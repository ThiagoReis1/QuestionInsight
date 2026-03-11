from numpy import*
e=array(eval(input("pessoas que entraram : ")))
s=array(eval(input("pessoas que sairam : ")))
i=0
a=(sum(e)-sum(s))
while(i > 0):
	i = i + 1
print(a)
	