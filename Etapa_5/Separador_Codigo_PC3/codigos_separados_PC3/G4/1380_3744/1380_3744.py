c= float(input("estimativa de carros por metro quadrado:"))
B= float(input("comprimento da base maior:"))
b= float(input("comprimento da base menor:"))
a= float(input("comprimento da altura:"))

A= a*(B+b)/2
Q= A*c
print(int(Q))