from numpy import *

temp=array(eval(input("Quais as medias: ")))

i=0
achou=0
while i<size(temp):
	if temp[i]<10 or 40<temp[i]:
		achou+=1
	i+=1
	
tempe=array(zeros(size(temp)-achou,dtype=float))
#print (tempe)

j=0
k=0
while j<size(temp):
	if 10<=temp[j] and temp[j] <=40:
		tempe[k]=temp[j]
		k+=1
	j+=1
	
print (tempe)