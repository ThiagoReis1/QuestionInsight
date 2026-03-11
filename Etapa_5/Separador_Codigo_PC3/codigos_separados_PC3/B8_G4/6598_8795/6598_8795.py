n=int(input())
tais=0
edgar=0
ana=0
c=0
while (c<n):
	l=input().lower()
	if (l=="tais"):
		tais=tais+1
	elif (l=="edgar"):
		edgar=edgar+1
	elif (l=="ana"):
		ana=ana+1
	c=c+1
print("tais=", tais)
print("edgar=", edgar)
print("ana=", ana)
