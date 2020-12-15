from itertools import combinations
import re

def ProcessInputList(items):
    for i in items:
        match = re.search(r'^([\d]+-[\d]+)\s([a-z]):\s([a-z]+)', i.strip())
        yield match.groups()
    # return [ match for i in items for match in re.search(r'^([\d]+-[\d]+)\s([a-z]):\s([a-z]+)', i.strip()) if match]

def Answer(part):
    if part == 1:
        num = 2
    else:
        num = 3

    with open("day2/input.txt", "r") as f:
        pChecks = list(ProcessInputList(f))
        countValid = 0
        for p in pChecks:
            if not p:
                continue
            min = int(p[0].split('-')[0])
            max = int(p[0].split('-')[1])
            if part == 1:
                count = p[2].count(p[1])
                if count >= min and count <= max:
                    countValid += 1
            else:
                min -= 1
                max -= 1
                if min < 0 or max >= len(p[2]) or p[2][min] == p[2][max]:
                    continue
                if p[2][min] == p[1] or p[2][max] == p[1]:
                    countValid += 1
        print(f"Part {part} Answer: {countValid}")
        # items = sorted(filter(lambda item: item <= 2020, [int(l.strip()) for l in f]))
        # subs = [comb for comb in combinations(items, num) if sum(comb) == 2020]

        # if len(subs):
        #     val = 1
        #     for x in list(subs[0]):
        #         val *= x
        #     print(f"Part {part} Answer: {val}")

if __name__ == "__main__":
    Answer(1)
    Answer(2)