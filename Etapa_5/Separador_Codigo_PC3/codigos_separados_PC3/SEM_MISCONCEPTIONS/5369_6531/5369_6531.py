from numpy import*
cpf = array(eval(input("Digite o numero: ")))
vet =array([9,8,7,6,5,4,3,2,1])
total_soma= cpf[0]*vet[0] + cpf[1]*vet[1] + cpf[2]*vet[2] + cpf[3]*vet[3] + cpf[4]*vet[4] + cpf[5]*vet[5] + cpf[6]*vet[6] + cpf[7]*vet[7] + cpf[8]*vet[8]
#print(total_soma)
newcpf = total_soma % 11
print(newcpf)