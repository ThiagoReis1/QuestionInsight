from numpy import*

v1 = array(eval(input("Digite as temperaturas: ")))

i = 0
count = 0
while(i < size(v1)):
	if(v1[i] >= 40) or (v1[i]<=10):
		count = count + 1
	i = i + 1
	
v2 = array(zeros(count, dtype = float))	
i = 0
count = 0
while(i < size(v1)):
	if(v1[i] >= 40) or (v1[i]<=10):
		count = count + 1		
	i = i + 1
else:
	v2 = v1
	
print(v2)