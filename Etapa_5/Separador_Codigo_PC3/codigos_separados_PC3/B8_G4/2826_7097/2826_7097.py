from numpy import*
nota=array(eval(input("")))
i=0
while i<size(nota):
	if nota[i]>8:
		nota[i]=10
	elif nota[i]<2:
		nota[i]=0
	i=i+1
print(nota)
