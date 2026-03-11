from numpy import*

n = array(eval(input("digite:")))
k =[1,2,3,4,5]

i = 0
while(i<size(n)):
	s = s + n[i]*k[i]
	i+=1
a = s / sum(k)
print(round(a,2))