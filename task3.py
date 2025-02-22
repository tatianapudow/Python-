def simmilar_elements(a,b):
    return[x for x in a if x in b]

a=[4,6,7,8,0,32,45,67,3]
b=[3,5,1,7,0,33,44]
print(simmilar_elements(a,b))
