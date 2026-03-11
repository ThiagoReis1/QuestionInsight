t=float(input("tempo de permanencia:"))

if t<2:
   x=5.00+1.25

elif t==2:
   x=5.00+2.25

else: 
   x=5.00+3.25

print(round(x, 2))
