def kangaroo(x1, v1, x2, v2):
    pos1 = x1
    pos2 = x2
    if v1 <= v2:
        return "NO"
    while pos1 < pos2:
        pos1 = pos1 + v1
        pos2 = pos2 + v2
        if pos1 == pos2:
            return "YES"
    return "NO"
        

    
    

print kangaroo(0, 3, 4, 2)
print kangaroo(0, 2, 5, 3)