a = "14+3/2*2"
a = a.split('/')
a.append("/")
for i in a:
    b = i.split('+')
    a[a.index(i)] = b
    # a[a.index(b)].append('+')

print(a)