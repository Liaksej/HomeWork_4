def dickt(string):
    k = {}
    for i in string:
        if i in k:
            k[i] += 1
        else:
            k[i]=1
    return k

u = 'abbccc'
print(dickt(u))
