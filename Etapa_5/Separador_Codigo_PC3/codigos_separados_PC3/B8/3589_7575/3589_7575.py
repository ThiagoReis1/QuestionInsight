from numpy import*

p=array(eval(input("Aneis acertados: ")))

i=0
total=0

while i<size(p):
	if(p[i]==1):
		total=total+80
	elif(p[i]==2):
		total=total+40
	elif(p[i]==3):
		total=total+20
	elif(p[i]==4):
		total=total+10
	i=i+1

print(total)