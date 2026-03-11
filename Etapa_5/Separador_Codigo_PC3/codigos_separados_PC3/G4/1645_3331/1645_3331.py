from numpy import*

s= array(eval(input("Saques: ")))

c=0

for i in range(size(s)):
	if s[i] >= 2000:
		c= c + 1
		s[i]=s[i]+1
print(c)

cont= zeros(c, dtype=int)

for i in range(size(s)):
	if i >= 2000:
		cont[0]=cont[0]+1
		i+=1
print(cont)