from numpy import*
v= array(eval(input("valores: ")))
i= 0
t = 0

while(i<size(v)):
		if(v[i]>90):
			t = t + v[i] - 6.5
		else:
			t = t + v[i]
		i = i +1
	
print(round(t,2))
