from numpy import*

v = array(eval(input("Digite o vetor:")))
x = array(zeros(2, dtipy=int))

A = min(v) 
B = max(v)

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

#i para x1
for x in v:
	if(v >= A):
		print(x)
#j para x2
for x in v:
	if(v >= C):
		print(x)
		
print(x)
		
	
	