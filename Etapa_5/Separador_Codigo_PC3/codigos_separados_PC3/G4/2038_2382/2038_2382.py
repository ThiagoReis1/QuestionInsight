r= input().upper()
n=0

while(r!="S"):
	while(r=="SIM"):
		n=n+1
		r=input()
	while(r=="NAO"):
		r=input()
print(n)