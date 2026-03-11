from numpy import*
s=input("Etinia: ").split(',')
new=zeros(5,dtype=int)

for i in range(size(s)):
	if s[i]=='B':
		new[0]+=1
	elif s[i]=='PA':
		new[1]+=1
	elif s[i]=='PR':
		new[2]+=1
	elif s[i]=='A':
		new[3]+=1
	elif s[i]=='I':
		new[4]+=1
print(max(new))
print(new)