from itertools import combinations

def Answer(part):
    slopes = [{"right":1, "down":1}]
    if part == 1:
        slopes = [{"right":3, "down": 1, "count": 0, "vert": 0, "horiz": 0}]
    else:
        slopes = []
        slopes.append({"right":1, "down":1, "count": 0, "vert": 0, "horiz": 0})
        slopes.append({"right":3, "down":1, "count": 0, "vert": 0, "horiz": 0})
        slopes.append({"right":5, "down":1, "count": 0, "vert": 0, "horiz": 0})
        slopes.append({"right":7, "down":1, "count": 0, "vert": 0, "horiz": 0})
        slopes.append({"right":1, "down":2, "count": 0, "vert": 0, "horiz": 0})
    with open("day3/input.txt", "r") as f:
        grid = [[c for c in l.strip()] for l in f.readlines()]
        page_width = len(grid[0])
        for slope in slopes:
            while slope['vert'] < len(grid):
                slope['count'] += (grid[slope['vert']][slope['horiz'] % page_width] == '#')
                slope['vert'] += slope['down']
                slope['horiz'] += slope['right']
        treeCounts = [slope['count'] for slope in slopes]
        if len(treeCounts):
            val = 1
            for x in treeCounts:
                val *= x
            print(f"Part {part} Answer: {val}")

if __name__ == "__main__":
    Answer(1)
    Answer(2)