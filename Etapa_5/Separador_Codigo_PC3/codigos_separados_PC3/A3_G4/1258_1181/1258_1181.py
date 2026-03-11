from numpy import*
p = float(imput("informe p:"))
x = array(eval(imput("informe x:")))
y = array(eval(imput("informe y:")))
t = p/9(p+1)
xt =0
yt =0
for i in range(size(x)):
	if(p>1):
		xt = xt +((abs(x[i]))**t)**(1/t)
		yt = yt +((abs(x[i]))**t)**(1/t)
	soma = xt +yt
print(round(soma,3))
	
	