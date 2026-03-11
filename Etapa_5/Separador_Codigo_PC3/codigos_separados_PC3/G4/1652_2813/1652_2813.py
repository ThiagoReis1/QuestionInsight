from numpy import*
x = input("").split(',')

b = 0
p = 0
r = 0
a = 0
n = 0

for i in range(size(x)):
	if(x[i].upper() == "B"):
		b = b + 1
	if(x[i].upper() == "PA"):
		p = p + 1
	if(x[i].upper() == "PR"):
		r = r + 1
	if(x[i].upper() == "A"):
		a = a + 1
	if(x[i].upper() == "I"):
		n = n + 1
		
if(b>p and b>r and b>a and b>n):
	print(b)
if(p>b and p>r and p>a and p>n):
	print(p)
if(r>b and r>p and r>a and r>n):
	print(r)
if(a>b and a>p and a>r and a>n):
	print(a)
if(n>b and n>p and n>r and n>a):
	print(n)
	
w = zeros(5,dtype=int)
w[0] = b
w[1] = p
w[2] = r
w[3] = a
w[4] = n 
print(w)