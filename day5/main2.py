stacks_raw = []
stacks_final = []
instructions = []

def get_stack_top(stacks):
    top = ''
    for stack in stacks:
        top += stack[-1]
    
    return top

def save_all_creates():
    colNums = [int(num) for num in stacks_raw[-1].split()]
    stacks = [[] for _ in colNums]

    for line in stacks_raw[:-1][::-1]:
        line_crates = line[1:len(line):4]
        for idx, crate in enumerate(line_crates):
            if crate != ' ':
                stacks[idx].append(crate)

    return stacks

def do_instructions(instructions, stacks):
    # instr: [move #, from #, to #]
    for instr in instructions:
        from_col = stacks[instr[1]-1]
        to_col = stacks[instr[2]-1]
        num_crates = instr[0]

        removed_crates = from_col[-num_crates:]
        stacks[instr[1]-1] = from_col[:-num_crates]
        to_col.extend(removed_crates)

with open('input.txt') as f:
    lines = f.readlines()
    reading_instructions = False

    for idx, line in enumerate(lines):
        if line == '\n':
            # crates end here and instructions start
            stacks_final = save_all_creates()
            reading_instructions = True
            continue

        if reading_instructions:
            instr = line.split()
            instructions.append([int(instr[1]), int(instr[3]), int(instr[5])])
        else:
            stacks_raw.append(line)

do_instructions(instructions, stacks_final)
print(get_stack_top(stacks_final))