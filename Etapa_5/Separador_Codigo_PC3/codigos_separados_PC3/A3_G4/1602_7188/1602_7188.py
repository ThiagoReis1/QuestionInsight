from numpy import*
tc= array(eval(input("tempo de chegada")))
i=0
t=0
while i< size(tc):
	if tc[i]== max(tc):
		t= i	
	i=i+1
print(t)