from numpy import*
cpf = array(eval(input("cpf: ")))
v = array([1,2,3,4,5,6,7,8,9])
u=cpf*v
t=sum(u)
print(t%11)
