from numpy import*
n = array(eval(input('digite um valor:')))
x = 0
for i in range(size(n)):
	if(n[i] > 80):			
		n[i] = n[i] - 5
x = sum(n)
print(round(x, 2))
		