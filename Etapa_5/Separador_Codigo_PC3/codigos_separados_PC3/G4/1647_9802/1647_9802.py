from numpy import*

al = array(eval(input("porcentagem dos alunos: ")))

ac = 0

for i in range(size(al)):
	if al[i] >= 70:
		ac = ac + 1
		
c = zeros(ac, dtype=int)
j = 0

for i in range(size(al)):
	if al[i] >= 70:
		c[j] = i
		j = j + 1
print(ac)
print(c)
	
		