from numpy import*
t = array(eval(input("Temperatura:")))
i = 0

n = 0
while(i < size(t)):
	if(t[i] >= 0):
		n = n + 1
	i = i + 1
t2 = array(zeros(n, dtype = float))
i = 0
j = 0
while(i < size(t)):
	if(t[i] >= 0):
		t2[j] = t[i]
		j = j + 1
	i = i + 1
print(t2)