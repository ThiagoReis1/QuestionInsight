s= input("s: ").lower()

i=0
a=0
c=0

while (i< len(s)):
	if(s[i] =='a') or(s[i] =='e') or(s[i] =='i') or(s[i] =='o') or(s[i] =='u'):
		a= a +1
	else:
		c=c+1
	i=i+1
		
custo = 0.15 * a + 0.17*c
print(custo)