v=float(input("qual o volume de agua consumido nesse mes?"))
total=(v*0.37+15)
icms=(total*35)/100
print(round(total+icms,2))
