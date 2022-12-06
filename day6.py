def main():
    with open('resources/day6.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(find_ind(data[0]))

def find_ind(s: str, length = 14):
    for i in range(len(s) - length):
        if not has_duplicate(s[i:i+length]):
            print("no dupes: " + s[i:i+length])
            return i + length

def has_duplicate(s: str):
    return len(s) != len(set(s))


if __name__ == "__main__":
    main()