from numpy import*
p=float(input())
t=p/(p-1)
x=array(eval(input()))
y=array(eval(input()))
soma=0
for i in range(size(x)):
	soma=soma+(abs(x[i]-y[i])**(t))
w=(soma)**(1/t)	
print(round(w,6))

