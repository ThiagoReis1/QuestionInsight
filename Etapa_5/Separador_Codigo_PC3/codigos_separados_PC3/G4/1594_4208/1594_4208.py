from numpy import*
dano=array(eval(input("")))
aa=size(dano)
i=0
total=0
j=1
while(i<aa):
	total=total+dano[i]*j
	j=j+1
	i=i+1
	
print(total)