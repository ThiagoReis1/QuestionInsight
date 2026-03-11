from numpy import*
v = array(eval(input()))
A = min(v)
B = max(v)
C = (0.75*A) + (0.25*B)
D = (0.25*A) + (0.75*B)
for i in v:
   x = zeros(2,dtype=int)
   for i in v:
      if (i>=C and i<D):
         x[0]=x[0]+1
      if (i>=D and i<B):
         x[1]=x[1]+1
print (x)
		
		