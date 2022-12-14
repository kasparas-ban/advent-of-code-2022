def findSameItem(line1, line2, line3):
    for l1 in line1:
        for l2 in line2:
            for l3 in line3:
                if l1 == l2 and l2 == l3:
                    return l1

def getPriority(letter):
    # 97 - 122 : 1 - 26
    # 65 - 90 : 27 - 52

    if ord(letter) >= 97 and ord(letter) <= 122:
        return ord(letter) - 96
    if ord(letter) >= 65 and ord(letter) <= 90:
        return ord(letter) - 64 + 26

    print("WHATS THIS: ", letter)

total = 0

with open('input.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        total += getPriority(findSameItem(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()))
        
print(total)