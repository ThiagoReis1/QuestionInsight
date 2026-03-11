q=int(input("quantidade inicial de grilos"))
x=int(input("quantidade de novos grilos treinados:"))
y=int(input("quantidade de novos grilos contaminados"))
t=0
while(q>0):
	q=q+x-y
	t=t+1
print(t)	