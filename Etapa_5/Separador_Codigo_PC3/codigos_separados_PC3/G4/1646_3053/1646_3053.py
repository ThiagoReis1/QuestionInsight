from numpy import*
v = array(eval(input("Valores: ")))

t = size(v)
a = 0

for i in range(t):
  if (v[i]<=50):
	  a = a + 1

v1 = zeros(a, dtype=int)
y = 0

for i in range(t):
	if (v[i]<=50):
		 v1[y] = i
		 y = y + 1
		
print(a)
print(v1)
	
	