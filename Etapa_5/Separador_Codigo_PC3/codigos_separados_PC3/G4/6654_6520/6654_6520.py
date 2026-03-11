from numpy import*

n=array(eval(input("notas: ")))
p=array([1,3,2,5])

i=0
num=0
dem=0

while i < size(n):
	num=num + n[i]*p[i]
	dem=dem + p[i]
result=num/dem
print(round(result,2))
	
	
	



