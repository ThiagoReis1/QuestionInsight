from numpy import*

x=array(eval(input("lista: ")))

cont=0

for i in range(1,size(x)):
	if x[i] <= -x[0] :
		print(i)
		cont+=1
		
print(cont)
	