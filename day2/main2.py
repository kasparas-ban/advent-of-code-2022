total_score = 0

lose_combinations = {
  'A': 'C',
  'B': 'A',
  'C': 'B'
}

win_combinations = {
  'A': 'B',
  'B': 'C',
  'C': 'A'
}

draw_combinations = {
  'A': 'A',
  'B': 'B',
  'C': 'C'
}


def get_sign_score(x):
    if x == 'A':
        return 1
    elif x == 'B':
        return 2
    elif x == 'C':
        return 3

def get_match_score(x, y):
  score = 0
  chosen_sign = ""

  if y == 'X': # need to lose
    score += 0
    chosen_sign = lose_combinations[x]
  elif y == 'Y': # need to draw
    score += 3
    chosen_sign = draw_combinations[x]
  elif y == 'Z': # need to win
    score += 6
    chosen_sign = win_combinations[x]

  score += get_sign_score(chosen_sign)
  return score

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        match = line.split()
        total_score += get_match_score(match[0], match[1])

print(total_score)
