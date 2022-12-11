top_elfs = [0, 0, 0]
current_cals = 0

with open('input.txt') as f: 
  for line in f:
    if line == '\n':
      if top_elfs[2] < current_cals:
        top_elfs.pop()
        top_elfs.append(current_cals)
        top_elfs.sort()
        top_elfs.reverse()
      current_cals = 0
    else:
      current_cals += int(line)

print(sum(top_elfs))
