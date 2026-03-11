#Gabriel Felipe
#25/08/16

from numpy import*
p = float(input("informe p:"))
x = array(eval(input("informe x:")))
y = array(eval(input("informe y:")))
t = p/(p+1)
xt =0
yt =0
for i in range(size(x)):
	if(p>1):
		xt = xt +((abs(x[i]))**t)**(1/t)
		yt = yt +((abs(x[i]))**t)**(1/t)
	soma = xt + yt
print(round(soma,4))