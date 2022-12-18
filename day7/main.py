class Dir:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.files = []
        self.dirs = {}

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir_name, dir):
        self.dirs[dir_name] = dir

    def __str__(self):
        return f"{self.name}(size: {self.size})(dirs: {self.dirs})(files: {self.files})"

class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name}({self.size})"

root_dir = Dir('/')
current_location = [root_dir]
result = 0

def calculates_sizes(dir):
    for f in dir.files:
        dir.size += f.size
    for d in dir.dirs:
        calculates_sizes(dir.dirs[d])
        dir.size += dir.dirs[d].size

def find_directories(dir, size_limit):
    global result
    if dir.size <= size_limit:
        result += dir.size
    for d in dir.dirs:
        find_directories(dir.dirs[d], size_limit)

def read_instr(line):
    if line == '$ ls':
        return
    if line == '$ cd ..':
        current_location.pop()
        return
    if line[0:4] == '$ cd':
        dir_name = line.split()[2]
        dir = current_location[-1].dirs[dir_name]
        current_location.append(dir)
        return
    
    [arg1, arg2] = line.split()

    if arg1 == 'dir':
        current_location[-1].add_dir(arg2, Dir(arg2))
    else:
        current_location[-1].add_file(File(arg2, int(arg1)))

with open('input.txt') as f:
    lines = f.readlines()[1:]
    for line in lines:
        read_instr(line.strip())

calculates_sizes(root_dir)
find_directories(root_dir, 100000)
print(result)