#s-t: location of house
#a: apple tree
#b: orange tree
#apples: list of where apples fall relative to apple tree
#oranges: list of where oranges fall relative to orange tree

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    for distance_a in apples:
        place = a + distance_a
        if s <= place <= t:
            appleCount = appleCount + 1
    for distance_b in oranges:
        placeB = b + distance_b
        if s <= placeB <= t:
            orangeCount = orangeCount + 1
    return appleCount, orangeCount


print countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])