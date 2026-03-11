num = input("digite um numero:")
v = num.split(',')
int_lst = [int(x) for x in v]
h = sum(int_lst)
print(h)
