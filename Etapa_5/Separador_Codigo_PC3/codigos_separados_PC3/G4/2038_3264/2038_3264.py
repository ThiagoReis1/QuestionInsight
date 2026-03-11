resp = input("")

a=0
n=0
resp2 = resp.upper()
while(resp2!="S"):
	if(resp2 =="SIM"):
		a = a + 1
	else:
		n = n+1
	resp = input("")
	resp2 = resp.upper()
print(a)
		