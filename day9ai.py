# Initialize the positions of the knots
head_pos = (0, 0)
knots = [(head_pos[0], head_pos[1])] * 10
trail = []

# Parse the input and simulate the movement of the rope
moves = open("resources/day9.txt", "r", encoding="utf-8").read().split("\n")
for move in moves:
  direction = move[0]
  steps = int(move[1:])

  # Update the position of the head
  if direction == "U":
    head_pos = (head_pos[0] - steps, head_pos[1])
  elif direction == "D":
    head_pos = (head_pos[0] + steps, head_pos[1])
  elif direction == "L":
    head_pos = (head_pos[0], head_pos[1] - steps)
  elif direction == "R":
    head_pos = (head_pos[0], head_pos[1] + steps)

  # Update the positions of the knots
  for i in range(9, 0, -1):
    knot_pos = knots[i-1]
    if abs(knot_pos[0] - knots[i][0]) <= 1 and abs(knot_pos[1] - knots[i][1]) <= 1:
      knots[i] = (knot_pos[0], knot_pos[1])
    else:
      if knot_pos[0] < knots[i][0]:
        knots[i] = (knots[i][0] - 1, knots[i][1])
      elif knot_pos[0] > knots[i][0]:
        knots[i] = (knots[i][0] + 1, knots[i][1])
      elif knot_pos[1] < knots[i][1]:
        knots[i] = (knots[i][0], knots[i][1] - 1)
      elif knot_pos[1] > knots[i][1]:
        knots[i] = (knots[i][0], knots[i][1] + 1)

  # Store the position of the last knot in the trail
  trail.append(knots[-1])

# Print the final positions of the knots
for knot in knots:
  print(knot)

# Print the trail of the last knot
print(trail)
