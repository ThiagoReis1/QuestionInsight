from numpy import*
base=array(eval(input("Vetor: ")))
base1=array(zeros(2,dtype=int))
a=min(base)
b=max(base)
c=(0.6*a) + (0.4*b)
d=(0.3*a) + (0.7*b)
for i in base:
	if (i>=a and i<c):
		base1[0]=base1[0]+1
	elif(i>=d and i<b):
		base1[1]=base1[1]+1
print(base1)