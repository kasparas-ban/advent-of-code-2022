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

total_available_space = 70000000
all_dirs = []

def calculates_sizes(dir):
    for f in dir.files:
        dir.size += f.size
    for d in dir.dirs:
        calculates_sizes(dir.dirs[d])
        dir.size += dir.dirs[d].size

def get_all_dirs(dir):
    all_dirs.append(dir)
    for d in dir.dirs:
        subdirs = get_all_dirs(dir.dirs[d])
        if subdirs != None:
            all_dirs.append(get_all_dirs(dir.dirs[d]))

def sort_all_dirs():
    all_dirs.sort(key=lambda x: x.size)

def select_dir_to_delete():
    taken_space = root_dir.size

    for d in all_dirs:
        if (total_available_space - taken_space) + d.size >= 30000000:
            return d.size
    return 0

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
get_all_dirs(root_dir)
sort_all_dirs()

print(select_dir_to_delete())