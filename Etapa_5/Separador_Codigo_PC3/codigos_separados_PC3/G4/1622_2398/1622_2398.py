from numpy import*
qe = array(eval(input()))
qs = array(eval(input()))
se = size(qe)
ss = size(qs)
i = 0
qt = 0
if(se==ss):
	while(i<se):
		qt = qt+(qe[i]-qs[i])
		i = i+1
	print(qt)