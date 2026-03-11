digitos = [9,8,7,6,5,4,3,2,1]

cpf = eval(input())

result=0

for i in range(len(digitos)):
   result+=digitos[i]*cpf[i]
print(result%11)