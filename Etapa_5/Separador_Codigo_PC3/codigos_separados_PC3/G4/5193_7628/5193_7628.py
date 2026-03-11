n=float(input())
a=float(input())
c=float(input())
d=float(input())

valor = n * 7.00 + a * 6.00 + c * 3.00 + d * 5.00

if (valor<=42.00):
   s=valor-3.00
else:
   s = valor-0.1*valor
   
print(round(s,2), "ryous")
   