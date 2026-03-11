from numpy import*
p=float(input("digite um numero real maior que 1: "))
x=array(eval(input("digite o primeiro vetor: ")))
y=array(eval(input("digite o segundo vetor: ")))
t=(p/(p-1))
tq=0
for i in range(size(x)):
	tq=tq+abs(x[i]-y[i])**t
n=(tq)**(1/t)
print(round(n, 6))