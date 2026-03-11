from numpy import*
x=array(eval(input("vetor: ")))
y=array(zeros(6,dtype=int))
i=0
for i in range (size(x)) :
	if(x[i]%2==0):
		print(x[i])
