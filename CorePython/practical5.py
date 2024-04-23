# given the nested dictonary grab the word "hello"
d = {
    'k1':[1,2,3,{'tricky':['oh', 'man', 'inception', {'target':[1,2,3,"hello"]}]}]
}

print(d.get('k1')[3].get('tricky')[3].get('target')[3])