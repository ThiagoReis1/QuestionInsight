A=int(input("quantidade inicial de baloes : "))
B=int(input("quantidade c : "))
C=int(input("quantidade d : "))
t=0

while (A<200):
	A=A+B-C
	t=t+1

print(t)