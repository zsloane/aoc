from itertools import combinations

def Answer(part):
    if part == 1:
        num = 2
    else:
        num = 3
    with open("day1/input.txt", "r") as f:
        items = sorted(filter(lambda item: item <= 2020, [int(l.strip()) for l in f]))
        subs = [comb for comb in combinations(items, num) if sum(comb) == 2020]

        if len(subs):
            val = 1
            for x in list(subs[0]):
                val *= x
            print(f"Part {part} Answer: {val}")

if __name__ == "__main__":
    Answer(1)
    Answer(2)