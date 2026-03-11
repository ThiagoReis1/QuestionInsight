x = input("letra")
x.upper()
acm = 0
n = "S"
while(x != n):
	if(x == "A"):
		acm += 1
	x = input("")
	x.upper()
		
print(acm)