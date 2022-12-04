def main():
    with open('resources/day2.txt', "r", encoding='utf-8') as file:
        text = file.readlines()
        points = 0
        for game in text:
            game = game.strip()
            mc = get_deciscion(game)
            game = game.split(" ")[0] + " " + mc
            result = get_result(game)
            points += get_points(mc, result)
        print(points)

def get_points(choice: str, result:int) -> int:
    pts = "XYZ".index(choice) + 1
    if result == 0:
        pts += 3
    elif result == 1:
        pts += 6
    return pts

def get_deciscion(a: str, b:str = None) -> str:
    if b is None:
        return get_deciscion(a.split(" ")[0], a.split(" ")[1])
    if b == 'X': # Lose
        return 'X' if a == 'B' else 'Y' if a == 'C' else 'Z'
    if b == 'Y': # Draw
        return chr(ord(a) + (ord('X') - ord('A')))
    if b == 'Z': # Win
        return 'X' if a == 'C' else 'Y' if a == 'A' else 'Z'

def get_result(a: str, b:str = None) -> int:
    if b is None:
        return get_result(a.split(" ")[0], a.split(" ")[1])
    if ord(b) - ord('X') == ord(a) - ord('A'):
        return 0
    if a == 'A':
        return 1 if b == 'Y' else -1
    if a == 'B':
        return 1 if b == 'Z' else -1
    return 1 if b == 'X' else -1

if __name__ == '__main__':
    main()