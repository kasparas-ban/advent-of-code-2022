def findSameItem(half1, half2):
    for l1 in half1:
        for l2 in half2:
            if l1 == l2:
                return l1

def getPriority(letter):
    # 97 - 122 : 1 - 26
    # 65 - 90 : 27 - 52

    if ord(letter) >= 97 and ord(letter) <= 122:
        return ord(letter) - 96
    if ord(letter) >= 65 and ord(letter) <= 90:
        return ord(letter) - 64 + 26

total = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        [half1, half2] = [line[:len(line)//2], line[len(line)//2:]]
        total += getPriority(findSameItem(half1, half2))
        
print(total)