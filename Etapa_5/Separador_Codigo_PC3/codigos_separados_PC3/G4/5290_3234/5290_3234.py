f=1
i=0
t=0
while(f!=-1):
	f=int(input("face do dado "))
	if(f!=-1):
		t=t+1
		if(f==5):
			i=i+1
print(t)
print(round(i/t*100,2))
