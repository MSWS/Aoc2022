elves = []
with open('resources/day1.txt', 'r', encoding='utf-8') as file:
  lines = file.readlines()
  big = 0
  for line in lines:
    if line == '\n':
      elves.append(big)
      big = 0
      continue
    big += int(line)
  if big != 0:
    elves.append(big)

elves.sort()
elves = list(reversed(elves))

print(elves)
print(elves[0] + elves[1] + elves[2])