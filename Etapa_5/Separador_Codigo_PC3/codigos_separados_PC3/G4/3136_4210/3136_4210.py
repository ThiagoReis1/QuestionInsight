from numpy import*
n = array(eval(input("vetor: ")))

i = 0
j = 0

while(i<size(n)):
	j = j + log(n[i]+1)
	i = i + 1
m = exp(j/size(n))-1
print(round(m,2))