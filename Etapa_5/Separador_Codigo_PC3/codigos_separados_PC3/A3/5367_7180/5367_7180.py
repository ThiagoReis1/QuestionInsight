from numpy import *

cpf = array(eval(input("Digite cpf: ")))

extra = [1,2,3,4,5,6,7,8,9]

total = cpf * extra

a = sum(total)

b = a % 11

c = a%100


print(b)
