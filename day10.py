def main():
  hist = []
  instruct = 0
  pending = 0
  registry = 1
  hist.append(registry)
  drawing = [""]
  with open("resources/day10.txt") as f:
    text = f.read()
    for line in text.split("\n"):
      hist.append(registry)
      # print(len(hist), registry)
      if line.startswith("add"):
        hist.append(registry)
        registry += int("".join(line.split(" ")[1:]))
        # hist.append(registry)
        print(len(hist), registry)
  for i, val in enumerate(hist):
    if i + 2 >= len(hist):
      break
    if abs((i % 40) - hist[i + 1]) > 1:
      drawing[-1] += "."
    else:
      drawing[-1] += "#"
    if len(drawing[-1]) >= 40:
      drawing.append("")
  print("\n".join(drawing))
  # total = 0
  # for i in range(20, 221, 40):
  #   print(i, hist[i])
  #   total += hist[i] * i
  # print(total)
if __name__ == "__main__":
  main()