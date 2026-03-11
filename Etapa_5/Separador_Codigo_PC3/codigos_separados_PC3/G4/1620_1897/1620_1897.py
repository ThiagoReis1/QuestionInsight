from numpy import*

t=array(eval(input("Tempo: ")))
p=array(eval(input("Vazão: ")))

l = zeros(size(t), dtype=float)
d = zeros(size(p), dtype=float)
i = 0
while(i<size(p)):
	d[i]=(p[i]/20)
	i=i+1

i = 0
while(i<size(l)):
	l[i]=(t[i]*d[i])
	i=i+1
print(round(sum(l),2))