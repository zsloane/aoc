from itertools import combinations

expected_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
allowed_missing = ["cid"]

import re

regex = r"([a-z]{3}(?=\:))\:([#0-9a-z]+?(?=\s|$))"

def validateField(f,v):
    if f == "byr":
        d = int(v)
        return d>=1920 and d<=2002
    elif f == "iyr":
        d = int(v)
        return d>=2010 and d<=2020
    elif f == "eyr":
        d = int(v)
        return d>=2020 and d<=2030
    elif f == "hgt":
        valid = r"([0-9]+)(cm|in)"
        matches = re.findall(valid,v)
        if len(matches) == 1:
            n,u = matches[0]
            if u == 'cm':
                d = int(n)
                return d>=150 and d<=193
            elif u == 'in':
                d = int(n)
                return d>=59 and d<=76
        return False
    elif f == "hcl":
        valid = r'^#[0-9a-f]{6}$'
        return len(re.findall(valid,v))
    elif f == "ecl":
        valid = r"^(amb|blu|brn|gry|grn|hzl|oth){1}$"
        return len(re.findall(valid,v))
        return True
    elif f == "pid":
        valid = r"^[0-9]{9}$"
        return len(re.findall(valid,v))
    elif f == "cid":
        return True
    else:
        return False

def group(seq, sep):
    g = []
    for el in seq:
        e=el.strip()
        if e == sep:
            yield ' '.join(g)
            g = []
            continue
        g.append(e)
    yield ' '.join(g)

def Answer(part):
    with open("day4/input.txt", "r") as f:
        passports = list(group((l.strip() for l in f.readlines()),''))
        # print(passports)
        countValid = 0
        for p in passports:
            matches = list(re.findall(regex, p))
            validMatches = []
            for k,v in matches:
                valid = validateField(k,v)
                if part == 1 or (part == 2 and valid):
                    validMatches.append(k)
            # validMatches = []
            fields = list(set(expected_fields) - set(validMatches)- set(allowed_missing))
            numMissing = len(fields)
            if not len(fields):
                countValid += 1
        print(f"Part {part} Answer: {countValid}")

if __name__ == "__main__":
    Answer(1)
    Answer(2)