from numpy import*
st= input("st: ").split(',')

P =0
C= 0
M= 0
V= 0
A = 0

for i in range(size(st)):
	if(st[i] == "P"):
		P= P +1
	if(st[i] == "C"):
		C= C +1
	if(st[i] == "M"):
		M= M +1
	if(st[i] == "V"):
		V= V +1
	if(st[i] == "A"):
		A =  A+1

s = zeros(5,dtype = int)

for i in range(size(s)):
	s[0]= P
	s[1]= C
	s[2]= M
	s[3]= V
	s[4]= A
	
print(max(P,C,M,V,A))
print(s)





