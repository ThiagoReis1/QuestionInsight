from numpy import*
x = array(eval(input("digite os valores: ")))
i = 0 
j = 0 
while(i< size(x)):
	if(x[i]>= 0.0 and x[i] <= 40.0):
		j = j+1
	i = i + 1
z = array(zeros(j, dtype = float))
i = 0
j = 0
while(i< size(x)):
	if(x[i]>= 0.0 and x[i] <= 40.0):
		z[j] = x[i]
		j = j + 1
	i = i + 1
print(z)
