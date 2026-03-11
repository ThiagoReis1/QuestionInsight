from numpy import *
n = array(eval(input()))
i = 0
med = 0
menor = min(n)
while(i < size(n)):
	if(n[i] != menor):
		med = med + n[i]
	i = i + 1
		
med = med/3
print(round(med,2))

if(med >= 5):
	print("APROVOU")
else:
	print("REPROVOU")