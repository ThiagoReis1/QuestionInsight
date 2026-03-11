from numpy import*

m = 0
b=0
c=0

l=array(eval(input()))

m = sum(l)/len(l)


for i in range (size(l)):
   b+= (l[i]-m)**2

c= (b/(len(l)-1))
d= c**(1/2)
print(round(d,3))