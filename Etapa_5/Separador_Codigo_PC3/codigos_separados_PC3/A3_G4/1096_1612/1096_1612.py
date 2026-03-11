x = int(input("propriedade x:"))

n1 = x//100000
n1 = x%100000
n2 = n1//1000
n2 = n2%1000
n3 = n2//1


y = (n1**3 + n2**3 + n3**3 )
z = n1+n2+n3


print(n1)
print(n2)
print(n3)
print(y)
