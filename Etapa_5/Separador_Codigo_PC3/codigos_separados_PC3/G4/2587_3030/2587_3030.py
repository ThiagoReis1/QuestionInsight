from numpy import*
v = array(eval(input("velocidade")))
uvm = v[0] + v[0]* 0.5
inf=0
for i in range(size(v)):
	if(v[i] > uvm):
		inf = inf+1
		print(i)
print(inf)