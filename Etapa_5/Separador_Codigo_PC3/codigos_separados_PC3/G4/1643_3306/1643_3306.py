from numpy import*
v= array(eval(input("medias:")))
aprov= 0
for i in v:
	if(i>=5):
		aprov+=1
cont= zeros(aprov,dtype=int)
t=0
for i in range(0,size(v)):
	if(v[i]>=5):
		cont[t]= i
		t+=1
print(aprov)
print(cont)