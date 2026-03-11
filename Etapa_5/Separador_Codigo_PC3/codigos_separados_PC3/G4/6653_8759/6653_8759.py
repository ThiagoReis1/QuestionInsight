from numpy import*
nota=array(eval(input()))
i=0
total= 0
pond= array([3,5,1])
while i< size(nota):
	total= (nota[i] * pond[i] ) + total
	i=i + 1
total= total / (3+ 5 + 1)
print(round(total,2))

