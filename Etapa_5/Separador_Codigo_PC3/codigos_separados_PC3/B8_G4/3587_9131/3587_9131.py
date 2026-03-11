from numpy import*
v = array(eval(input("")))
s = size(v)
i = 0
p = 100
while s > i:
   if v[i] == 1:
      p = p*5
   elif v[i] == 2:
      p = p*3
   elif v[i] == 4:
      p = p/2
   i += 1
print(round(p, 2))