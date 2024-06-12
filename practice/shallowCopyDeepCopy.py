import copy

a=[[1],2,3,54,5,6,7,78,8,9,9.12]

b=copy.copy(a)
c=copy.deepcopy(a)
print(a,b,c)
b[0][0]="a"
b.append(120)
c[0][0]="b"
c.append(140)
print(a,b,c)

