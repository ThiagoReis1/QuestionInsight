# faça seu código aqui!
s=input().upper()
x=0
y=0

while x!=len(s):
	if s[x]=='E':
		y+=1
	x+=1
print(y)