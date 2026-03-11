#Universidade Federal do Amazonas
#Everaldo Oliveira Silva - matricula 21453644

from numpy import*
p=float(input("digite p: "))
x=array(eval(input("digite x: ")))
y=array(eval(input("digite y: ")))
t=p/(p-1)
s=0
for i in range (size(x)):
	s+=abs(2*x[i] + 3*y[i])**t
d=(s)**(1/t)
print(round(d,3))