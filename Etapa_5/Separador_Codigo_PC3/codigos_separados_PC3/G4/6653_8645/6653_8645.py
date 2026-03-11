from numpy import*

v=array(eval(input("v: ")))
p=array([3,5,1])

t = 0
i = 0
while i < size(v):
	t = t + (v[i]*p[i])
	i = i + 1

t1 = t/sum(p)
print(round(t1, 2))