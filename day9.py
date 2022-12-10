PATH = [x.split() for x in open("resources/day9.txt").readlines()]

VISITED_LOC = set()

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def R(self):
    return Point(self.x+1, self.y)
  def L(self):
    return Point(self.x-1, self.y)
  def U(self):
    return Point(self.x, self.y+1)
  def D(self):
    return Point(self.x, self.y-1)
  def move(self, diff):
    xdir = -1 if diff.x < 0 else 1
    ydir = -1 if diff.y < 0 else 1
    if abs(diff.x) > 1 and diff.y == 0:
      return Point(self.x + xdir, self.y)
    elif diff.x == 0 and abs(diff.y) > 1:
      return Point(self.x, self.y + ydir)
    elif abs(diff.x) > 1 or abs(diff.y) > 1:
      return Point(self.x + xdir, self.y + ydir)
    else:
      return self
  def __sub__(self, other):
    return Point(self.x-other.x, self.y-other.y)
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)
  def __hash__(self):
    return hash((self.x, self.y))
  def __repr__(self):
    return f"Point({self.x},{self.y})"

def main(n):
  # convert array to bunch of string. ex: ['R', '4'] = RRRR
  fullpath = ''.join([c[0] * int(c[1]) for c in PATH])
  points = [Point(0,0) for i in range(n)]
  for path in fullpath:
    points[0] = getattr(points[0], path)()
    for i in range(n-1):
      h,t = points[i:i+2]
      diff = h-t
      t = t.move(diff)
      # print(i, h, t, diff)
      points[i]=h
      points[i+1]=t
    VISITED_LOC.add(points[-1])

main(10)

print(f'Solution 2: {len(VISITED_LOC)}')
