pinicial=int(input())
taxa=float(input())
num=int(input())
t=1
p=(((pinicial*taxa)/100)-num)

while   p>0 :
	
	pinicial=pinicial+p
	t=t+1
print(t)	