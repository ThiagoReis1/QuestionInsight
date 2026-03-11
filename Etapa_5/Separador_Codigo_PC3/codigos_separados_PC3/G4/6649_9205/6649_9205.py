from numpy import*

n= array(eval(input()))
p= array([3.0,2.0,4.0,1.0,3.0])
somat = sum(p)
i= 0 
while(i<size(n)):
	n[i]= n[i]* p [i]
	i+=1
	
soma= sum(n)
med= soma/somat
print(round(med,2))