from numpy import*

fc=array(eval(input("Face do Dado: ")))
i=0
total=0
while i<size(fc):
	if fc[i]==1:
		total+=10
	elif fc[i]==2:
		total+=5
	elif fc[i]==4:
		total+=5
	elif fc[i]==5:
		total+=20
	elif fc[i]==6:
		total+=10
	i+=1
print(total)