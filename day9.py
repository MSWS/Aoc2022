import enum
import math

head = [0, 0]
tail = [[0, 0] for i in range(10)]
hist = set()

class Direction(enum.Enum):
  NORTH = 0
  EAST = 1
  SOUTH = 2
  WEST = 3

def main():
  with open("resources/day9.txt", "r", encoding="utf-8") as f:
    steps = f.read().split("\n")
    for step in steps:
      direction = get_direction(step.split(" ")[0])
      dist = int(step.split(" ")[1])
      for i in range(dist):
        old_loc = head
        move_head(direction)
        check_tail(tail, old_loc, direction, math.sqrt(2))
        hist.add((tail[-1][0], tail[-1][1]))
    print("Result:", len(hist))

def move_head(dir: Direction):
  global head
  if dir == Direction.NORTH:
    head = (head[0], head[1] + 1)
  elif dir == Direction.EAST:
    head = (head[0] + 1, head[1])
  elif dir == Direction.SOUTH:
    head = (head[0], head[1] - 1)
  elif dir == Direction.WEST:
    head = (head[0] - 1, head[1])

def check_tail(tail, oldpos: [int], move_dir: Direction, max_dist_from_head: int):
  if get_dist(head[0], head[1], tail[0][0], tail[0][1]) <= max_dist_from_head:
    return
  tmppos = tail[0]
  tail[0] = oldpos
  oldpos = tmppos
  for i in range(1, len(tail)):
    if get_dist(tail[i-1][0], tail[i-1][1], tail[i][0], tail[i][1]) <= max_dist_from_head:
      break
    tmppos = tail[i]
    tail[i] = oldpos
    oldpos = tmppos

def get_dist(x1, y1, x2, y2):
  return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_direction(c: str):
  # Create a match statement to match ULDR
  match c:
    case "U":
      return Direction.NORTH
    case "L":
      return Direction.WEST
    case "D":
      return Direction.SOUTH
    case "R":
      return Direction.EAST
  print("unknown direction:", c)

if __name__ == "__main__":
  main()