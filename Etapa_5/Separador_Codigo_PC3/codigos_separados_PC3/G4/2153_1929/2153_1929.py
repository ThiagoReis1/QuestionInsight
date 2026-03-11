from numpy import*
p = array(eval(input("vetor p: ")))
q = array(eval(input("vetor q:")))
dist = 0.0
for i in range(size(p)):
	
	dist = sqrt(dist + sqrt(((p[i]- q[i])**2)*(p[i] - q[i])**2))

print(round(dist,4))