n = int(input("digite um numero inteiro positivo: "))
i = 0
m = 0
while(n!=0):
	if(n>0):
		i = i+1
		if(n%3==0):
			m = m+1
	n = int(input("digite um numero inteiro:"))
P = (m/i)*100	
print(i)
print(round(P,2))