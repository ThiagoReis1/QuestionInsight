from numpy import*
a=array(eval(input("insira as notas")))
i=0
while(i<size(a)):
	i=i+1
	c=(sum(a)- min(a))/(size(a)-1)

print(round(c,2))
				  