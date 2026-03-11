x = int(input("Idade: "))
i=0
t=0
while x!=-1:
	if x<18:
		i=i+1
	t=t+1
	x=int(input("Idade: "))
print(t)
print(round(100*i/t,2))