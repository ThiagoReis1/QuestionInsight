from numpy import*

CPF = array(eval(input("Digite 9 numeros do CPF: ")))
v = array([9,8,7,6,5,4,3,2,1])

soma = CPF * v

y = sum(soma)
print(y%11)