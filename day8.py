# def main():
#     with open("resources/day8.txt", "r") as f:
#         trees = f.readlines()
#         visible = 0
#         trees = [x.strip() for x in trees]
#         for y, val in enumerate(trees):
#             for x in range(len(trees[y])):
#                 rightEdge = trees[y][x:]
#                 if is_visible(rightEdge):
#                     visible += 1
#                     continue
#                 leftEdge = trees[y][:x + 1]
#                 leftEdge = leftEdge[::-1]
#                 # print(leftEdge)
#                 if is_visible(leftEdge):
#                     visible += 1
#                     continue
#                 topEdge = ""
#                 for ty in range(y + 1):
#                     topEdge += trees[ty][x]
#                 topEdge = topEdge[::-1]
#                 # print(topEdge)
#                 if is_visible(topEdge.strip()):
#                     visible += 1
#                     continue
#                 bottomEdge = ""
#                 for ty in range(len(trees) - 1, y - 1, -1):
#                     bottomEdge += trees[ty][x]
#                 bottomEdge = bottomEdge[::-1]
#                 # print(bottomEdge)
#                 if is_visible(bottomEdge.strip()):
#                     visible += 1
#                     continue
#         print(visible)

def main():
    with open("resources/day8.txt", "r") as f:
        trees = f.readlines()
        visible = 0
        trees = [x.strip() for x in trees]
        highest = 0
        for y, val in enumerate(trees):
            for x in range(len(trees[y])):
                rightEdge = trees[y][x:]
                score = get_score(rightEdge)
                leftEdge = trees[y][:x + 1]
                leftEdge = leftEdge[::-1]
                score *= get_score(leftEdge)
                topEdge = ""
                for ty in range(y + 1):
                    topEdge += trees[ty][x]
                topEdge = topEdge[::-1]
                score *= get_score(topEdge)
                bottomEdge = ""
                for ty in range(len(trees) - 1, y - 1, -1):
                    bottomEdge += trees[ty][x]
                bottomEdge = bottomEdge[::-1]
                # print(bottomEdge)
                score *= get_score(bottomEdge)
                if score > highest:
                    highest = score
        print(highest)

def get_score(trees: str):
    trees = trees.strip()
    trees = trees.replace("\n", "")
    if trees == "\n" or trees == "":
        return False
    score = 0
    heights = [int(x) for x in trees]
    for i in heights[1:]:
        if i < heights[0]:
            score += 1
        else:
            return score + 1
    return score

def is_visible(trees: str):
    # print("Checking visibility of: " + trees)
    trees = trees.strip()
    trees = trees.replace("\n", "")
    if trees == "\n" or trees == "":
        return False
    
    heights = [int(x) for x in trees]
    for i in heights[1:]:
        if i >= heights[0]:
            return False
    return True

if __name__ == '__main__':
    main()