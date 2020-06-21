n =(input("Enter a string "))
L = ['i','i','i','i','s','s','s','s','p','p','m']

dict = {}

for x in L:
    if x in dict:
        dict[x] = dict[x] + 1
    else:
        dict[x] = 1

def g(k):
    return dict[k]

y = sorted(dict.keys(), key=lambda k: dict[k], reverse = True)
for k in y:
    print("{} = {} ".format(k,dict[k]))
