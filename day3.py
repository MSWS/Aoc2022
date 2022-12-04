def main():
    with open("resources/day3.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        priors = 0
        group = []
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            group.append(line)
            if len(group) == 3:
                dupe = get_duplicate(group)
                print(dupe)
                priors += get_priority(dupe)
                group = []
                continue
        print(priors)

def get_duplicate(strings: list[str]):
    while len(strings[0][0]) > 0:
        match = True
        for s in strings[1:]:
            if strings[0][0] not in s:
                strings[0] = strings[0][1:]
                match = False
                break
        if not match:
            continue
        return strings[0][0]

def get_priority(char: str) -> int:
    return ord(char) - (ord('A') if char.isupper() else ord('a')) + (27 if char.isupper() else 1)

if __name__ == "__main__":
    main()