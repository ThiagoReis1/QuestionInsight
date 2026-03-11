x=int(input("numero inteiro:"))
y=int(input("numero inteiro"))

ac=0

while x <= y :
	if x % 7 == 0:
		ac=ac +x
	x=x+1
		
print(ac)
		