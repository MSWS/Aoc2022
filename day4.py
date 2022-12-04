def main():
    with open("resources/day4.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        cnt = 0
        for ranges in lines:
            ranges = ranges.strip()
            a = parse_range(ranges.split(",")[0])
            b = parse_range(ranges.split(",")[1])
            if contains(a, b):
              cnt += 1
        print(cnt)

def parse_range(s: str) -> (int, int):
    return (int(s.split("-")[0]), int(s.split("-")[1]))

def contains(a: (int, int), b: (int, int)) -> bool:
    if a[0] <= b[0] and a[1] >= b[0]:
        return True
    if a[0] <= b[1] and a[0] >= b[0]:
        return True
    return False

if __name__ == "__main__":
  main()