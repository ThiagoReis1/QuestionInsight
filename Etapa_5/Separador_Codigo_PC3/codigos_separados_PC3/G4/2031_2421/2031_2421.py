n=int(input("numero do dado: "))
t=0
while (n != -1):
	if(n==6):
		t=t+1
	n=int(input("proxima entrada: "))
print(t)
