def checkOverlap(sec1, sec2):
    [min1, max1] = sec1.split('-')
    [min2, max2] = sec2.split('-')
    if (int(min1) <= int(min2) and int(max1) >= int(min2)) or (int(min2) <= int(min1) and int(max2) >= int(min1)):
        return 1
    return 0
    

# def checkContains(sec1, sec2):
#     [min1, max1] = sec1.split('-')
#     [min2, max2] = sec2.split('-')
#     if (int(min1) >= int(min2) and int(max1) <= int(max2)) or (int(min2) >= int(min1) and int(max2) <= int(max1)):
#         return 1
#     return 0

total = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        [sec1, sec2] = line.split(',')
        total += checkOverlap(sec1, sec2)

print(total)
