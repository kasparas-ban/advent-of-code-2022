total_score = 1

scores = {
  'AX': 3,
  'BX': 0,
  'CX': 6,
  'AY': 6,
  'BY': 3,
  'CY': 0,
  'AZ': 0,
  'BZ': 6,
  'CZ': 3
}

def get_match_score(x, y):
    score = 0
    if y == 'X':
	    score += 1
    elif y == 'Y':
        score += 2
    elif y == 'Z':
        score += 3

    score += scores[x+y]
    return score



with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        match = line.split()
        total_score += get_match_score(match[0], match[1])

print(total_score)
