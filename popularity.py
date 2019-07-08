def friends(n):
    friends = {"Bob": ["Fred"], 'Fred': ['Bob', 'Charlie'], 'Charlie': ['Fred', 'Edgar', 'Diana'], 'Edgar': ['Alice', 'Fred'], 'Diana': ['Alice'], 'Alice': ['Bob', 'Diana', 'Edgar'] }
    #print friends.get(n)
    return friends[n]


def popularity(t,p):
    if t == 0:
        return 1
    else:
        score = 0
        for f in friends(p):
            score = score + popularity(t - 1, f)
        return score




print popularity(10,'Bob')
# print friends("Fred")