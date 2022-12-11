cal_list = []

with open('input.txt') as f:
  cals = 0  
  for line in f:
    if line == '\n':
      cal_list.append(cals)
      cals = 0
    else:
      cals += int(line)

print(max(cal_list))
