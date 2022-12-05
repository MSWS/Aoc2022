crates = []

def main():
    with open("resources/day5.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        index = lines.index("\n")
        parse_crates(lines[:index])
        for crate in crates:
            print(len(crate), crate)
        # print(crates)
        for line in lines[index+1:]:
            parse_instruction(line)
        for crate in crates:
            if len(crate):
                print(crate[0], end="")
  

def parse_crates(lines: list[str]):
    for i in range(len(lines[0])):
        crates.append([])
    for line in lines:
        line = line[:-1]
        for ind, l in enumerate(line):
            if(l == ' '):
                continue
            crates[ind].append(line[ind])

def parse_instruction(line: str):
    arr = line.split(" ")
    times = int(arr[1])
    src = int(arr[3]) - 1
    tar = int(arr[5]) - 1
    # for i in range(times): # Part 1
    #   crates[tar].insert(0, crates[src].pop(0))
    crates[tar] = crates[src][:times] + crates[tar]
    crates[src] = crates[src][times:]


if __name__ == '__main__':
    main()