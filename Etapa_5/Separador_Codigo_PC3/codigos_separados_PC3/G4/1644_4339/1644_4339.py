from numpy import*
ve= array(eval(input("valores do vetor:")))
i=0

for x in range (size(ve)):
	if ve[x] < 5.0:
		i=i + 1
tor= zeros(i,dtype=int)
print(i)
j=0
for x in range(len(ve)):
	if ve[x] < 5.0:
		tor[j]= x
		j= j + 1
	
print(tor)