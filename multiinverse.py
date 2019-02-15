def multiinverse(a,m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 1:
      return 0
 
    while a>1:
        # q is quotient
        q = a // m
        t = int(m)
        # m is remainder now, process same as
        # Euclid's algo
        m = (a % m)
        a= t
        t = x0
        x0 = x1 - (q * x0)
        x1 = t
    if a==None:
        a=0
 
    # Make x1 positive
    if (x1 < 0):
       x1 += m0
 
    return x1
x=multiinverse(4,11)
print(x)
