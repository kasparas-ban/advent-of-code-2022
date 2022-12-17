def contains_duplicates(chars):
    new_str = ''
    for char in chars:
        if char in new_str:
            return True
        else:
            new_str += char

    return False

num_chars = 0

with open('input.txt') as f:
    text = f.readlines()[0]
    i = 0
    test_str = ''

    for idx, char in enumerate(text):
        test_str += char

        if contains_duplicates(test_str):
            test_str = char

        if len(test_str) == 4:
            num_chars = idx
            break

print(num_chars+1)