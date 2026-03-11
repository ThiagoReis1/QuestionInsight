from numpy import*

vetor=array(eval(input()))
peso= array([1,2,3])
total= 0 
mamae =1
for i in vetor:
	
	total= total + i * mamae
	mamae = mamae +1
print(total)




