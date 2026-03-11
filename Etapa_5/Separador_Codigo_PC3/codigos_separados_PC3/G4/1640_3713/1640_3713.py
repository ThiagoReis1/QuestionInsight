from numpy import*
n = array(eval(input()))
t = 0
y=0
imp=0
while t<size(n):
	if n[t]%2!=0:
		imp=imp+1
	t+=1
t=0
x=zeros(imp, dtype=int)
while t<size(n):
	if n[t]%2==1:
		x[y]=t
		y+=1
	t+=1
print(imp)
print(x)


