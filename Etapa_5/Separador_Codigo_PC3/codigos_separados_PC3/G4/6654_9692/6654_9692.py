from numpy import*
n = array(eval(input("insira o vetor de notas: ")))
x = [1,3,2,5]
t = len(n)-1
i = 0
s = 0
while i<= t:
	s = s + n[i]*x[i]
	
	i +=1
m = s/sum(x)
print(round(m,2))