from numpy import*
x=input("String aqui:")
y=x.split(',')
z=zeros(size(y), dtype=int)
i = 0

while i < size(y):
	z[i] = int(y[i])
	i = i + 1
print(sum(z))