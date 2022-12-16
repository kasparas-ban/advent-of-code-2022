stacksRaw = []
stacksFinal = []
instructions = []

def getStackTop(stacks):
    top = ''
    for stack in stacks:
        top += stack[-1]
    
    return top

def saveAllCreates():
    colNums = [int(num) for num in stacksRaw[-1].split()]
    stacks = [[] for _ in colNums]

    for line in stacksRaw[:-1][::-1]:
        lineCrates = line[1:len(line):4]
        for idx, crate in enumerate(lineCrates):
            if crate != ' ':
                stacks[idx].append(crate)

    return stacks

def doInstructions(instructions, stacks):
    # instr: [move #, from #, to #]
    for instr in instructions:
        fromCol = stacks[instr[1]-1]
        toCol = stacks[instr[2]-1]
        for _ in range(instr[0]):
            removed_crate = fromCol.pop(-1)
            toCol.append(removed_crate)

with open('input.txt') as f:
    lines = f.readlines()
    reading_instructions = False

    for idx, line in enumerate(lines):
        if line == '\n':
            # crates end here and instructions start
            stacksFinal = saveAllCreates()
            reading_instructions = True
            continue

        if reading_instructions:
            instr = line.split()
            instructions.append([int(instr[1]), int(instr[3]), int(instr[5])])
        else:
            stacksRaw.append(line)

doInstructions(instructions, stacksFinal)
print(getStackTop(stacksFinal))