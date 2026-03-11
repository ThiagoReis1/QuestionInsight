from numpy import*
v1=array(eval(input("tempo de banho: ")))
v2=array(eval(input("modo de banho: ")))
i=0
q=0
m=0
f=0
while i<size(v2):
	if(v2[i]=="QUENTE"):
		q=q+1
	elif(v2[i]=="MORNO"):
		m=m+1
	elif(v2[i]=="FRIO"):
		f=f+1
	i=i+1