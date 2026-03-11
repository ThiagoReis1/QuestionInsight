from numpy import*
v = array(eval(input('Insira as notas:')))
t=0
for i in range (size(v)):
	if v[i]<5:
		t+=1

y=0
x=zeros(t,dtype=int)
for i in range (size(v)):
	if v[i]<5:
		x[y]=i
		y+=1

print(t)
print(x)