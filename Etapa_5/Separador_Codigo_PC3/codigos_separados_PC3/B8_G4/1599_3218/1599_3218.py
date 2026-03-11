from numpy import*
v=array(eval(input()))
i=0
d=[]
while(i<size(v)):
		if(v[i]>80):
			c=(v[i])-0.15
		elif(v[i]<80):
			c=(v[i])
		i+=1
		d=d+c
print(round(sum(d),2))
			
print()
			
		
