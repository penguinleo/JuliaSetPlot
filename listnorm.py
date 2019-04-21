from listmax import listmax
def listnorm(a = [],m = 10):
    a_len = len(a)
    max = listmax(a)
    b=[]
    for x in range(0,a_len):
        b.append(int(a[x]/max*m))
        pass
    return b
    pass