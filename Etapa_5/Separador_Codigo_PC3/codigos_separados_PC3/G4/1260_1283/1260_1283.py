from numpy import*
a=float(input("Primeiro:"))
b=array(eval(input("Segundo:")))
c=array(eval(input("Terceiro:")))
d=array(zeros(size(b),dtype=float))
t=a/(a+1)
for i in range(size(b)):
	d[i]=c[i]-b[i]
norma=0
for j in range(size(d)):
	norma= norma+abs(d[j])**t
norma= norma**(1/t)
x=norma
print(round(x,4))
