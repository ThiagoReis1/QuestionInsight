from numpy import*
v=array(eval(input("num de alunos das turmas:")))
num=0
for i in v:
	if(i%3==0):
		num=num+1
print(num)
print(v)