from numpy import*
v = array(eval(input(" temperatura:")))
i = 0
inv = 0
while(i < size(v)):
  if(v[i] > 40 or v[i] < (0)):
    inv = inv + 1
  i = i +1  
v1 = array(zeros(size(v) - inv, dtype=int))
i = 0
j = 0
while(i < size(v)):
  if(v[i] < 40 or v[i] > (0)):
    v1[j] = v[i]
    j=j+1
  i = i+1
print(v1)