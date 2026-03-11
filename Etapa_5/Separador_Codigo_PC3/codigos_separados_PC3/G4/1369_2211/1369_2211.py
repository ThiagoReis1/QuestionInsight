#necessarios 3 ingredientes

#01 - 4g de chifre de touro = CT

#02 - 3.14g de gramas de ouro em pó = GO

#03 - 10g de oleo de swarvem = OS

#escrever algo que leia na ordem a quantidade...
#...disponivel. usar "min()"


CT=4
GO=3.14
OS=10

a=float(input("quantidade disponivel de CT:"))
b=float(input("quantidade disponivel de GO:"))
c=float(input("quantidade disponivel de OS:"))

a1=a//CT
b1=b//GO
c1=c//OS

print (int(min(a1,b1,c1)))