from numpy import*

p= array(eval(input('1: ')))
q= array(eval(input('2: ')))

i=0
s=0
while(i< size(p)):
	s = s + (p[i] - q[i])**2
	i= i+1
	
print(round((s)**0.5,4))

sim = 1 / (1 + (s)**0.5)
print(round(sim,2))