def lonelyinteger(a):
    for n in a:
        count = 0
        for e in a:
            if n == e:
                count = count + 1
        if count == 1:
            return n
     
 
        

print lonelyinteger([0, 0, 1, 2, 1])
print lonelyinteger([1, 1, 2])
print lonelyinteger([1])
print lonelyinteger([2,3,2])