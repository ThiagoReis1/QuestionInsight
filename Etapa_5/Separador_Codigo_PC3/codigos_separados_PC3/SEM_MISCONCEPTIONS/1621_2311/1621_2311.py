from numpy import*
ARROZ = 1.25
FEIJAO = 2.60
BIS = 1.80
MIOJO = 0.85
FANTA = 3.20
n = array(eval(input()))
v = array(eval(input()))
i = 0
w = 0
while i < size(v):
    if n[i] == "ARROZ":
        W= w + ARROZ*v[i]
        i += 1   
   elif n[i] == "FEIJAO":   
        w= w + FEIJAO*v[i]
         i += 1
   elif n[i] == "BIS":
        w= w + BIS*v[i]
         i += 1
   elif n[i] == "MIOJO":
        w= w + MIOJO*v[i]
         i += 1   
   elif n[i] == "FANTA":
       w= w + FANTA*v[i]
         i += 1   
print(round(w,2))