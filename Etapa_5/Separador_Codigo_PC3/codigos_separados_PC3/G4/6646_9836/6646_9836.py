from numpy import*
var=array(eval(input("")))
p= ([1,2,3])
i=0
num=0
while i < size (var):
	num += var[i]*p[i]
	i += 1
media = num/sum(p) 

print(round(media,2))



