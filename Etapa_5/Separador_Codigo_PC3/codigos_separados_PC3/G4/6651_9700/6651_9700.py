from numpy import *
s = [5,4,3,2]
vet =array(eval(input()))
if size(vet) == size(s):
	media=0
	i=0
	a=0
	
	while i < size(vet):
		media=media+(vet[i]*s[i])
		a=a+s[i]
		i=i+1
	print(round(media/a,2))


	




