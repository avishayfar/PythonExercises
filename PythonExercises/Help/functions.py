

def targil_modoule():
    list = []
    for i in range(0,100):
        if(i%7 == 0 ) and (i%5 ==0) :
            list.append(i)
    print (list)


def fact(x):
    if (x == 0):
        return 1
    return x * fact(x-1)


def factory(x):
    fct = fact(x)
    print(fct)



def buildDict(n):
    d = dict()
    for i in range(1,n):
        d[i] = i*i +8
    print(d)
        
