from numpy import*
num = array(eval(input("insira ")))
a1 = 0
a2 = 0
a3 = 0
a4 = 0
x = [1,2,3,4]
t = size(num)-1
i = 0
while i<=t:
	if num[i] == 1:
		a1 = a1 + 1
	elif num[i] == 2:
		a2 = a2 + 1
	elif num[i] ==3:
		a3 = a3 + 1
	elif num[i] == 4:
		a4 = a4 +1
		
	i+=1
v = a1*80 + a2*40 + a3*20 +a4*10
print(v)
		
		
		
	