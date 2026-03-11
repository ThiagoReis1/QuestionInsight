from numpy import*
cpf=array(eval(input("digite o cpf senhora:  ")))
aux=array([1,2,3,4,5,6,7,8,9])
mult=cpf[0]*aux[0]+cpf[1]*aux[1]+cpf[2]*aux[2]+cpf[3]*aux[3]+cpf[4]*aux[4]+cpf[5]*aux[5]+cpf[6]*aux[6]+cpf[7]*aux[7]+cpf[8]*aux[8]
print(mult%11)