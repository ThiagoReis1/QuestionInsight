from numpy import*
acid = array(eval(input()))
i = 0
j = 0
for i in range(size(acid)): 
	if(acid[i]<acid[0]):
		j = j + 1
		print(i)
	i = i +1
	
print(j)
		