from numpy import*
v=array(eval(input("qual o vetor: ")))
i=1
a=0
while(i<size(v)):
	a=a+v[i]+v[i-1]
	print(a)
	i=i+1

print(a)
    