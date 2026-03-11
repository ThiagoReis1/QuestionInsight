from numpy import*
v= array(eval(input("acidentes minimos:"))) #v1[0]= numero minimo de acidentes
t= 0 
cont= zeros(size(v), dtype=int)
for i in range(1,size(v)):
		if(v[i]>=v[0]):
			print(i)
			t=t+1
print(t)
		
		