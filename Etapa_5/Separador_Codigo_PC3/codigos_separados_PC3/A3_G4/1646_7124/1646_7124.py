from numpy import*
s= array(eval(input("")))
cont = 0

vet= zeros(size(s), dtype = int)
for i in (range(size(s))):
	if s[i]<= 50:
		cont= cont+1
print (cont)

vet= zeros(cont,dtype= int)
c=0
for i in range(size(s)):
	if s[i]<=50:
		vet[c]=i
		c=c+1
print(vet)
		
		