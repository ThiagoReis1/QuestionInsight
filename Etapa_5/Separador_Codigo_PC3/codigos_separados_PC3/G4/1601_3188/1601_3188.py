from numpy import*

v=array(eval(input("escreva: ")))


for i in range(size(v)):
	if v[i]==min(v):
		print(i)
	
	