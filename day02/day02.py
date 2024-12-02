levels = []
with open('./day02.txt', 'r') as file:
    for line in file:
        level = line.split()
        levels.append([int(num) for num in level])

def less_than(a, b):
    return a < b

def grater_than(a, b):
    return a > b

def is_safe(level, cmp):
    for i in range(1, len(level)):
        if not (cmp(level[i-1], level[i]) and 1 <= abs(level[i-1] - level[i]) <= 3):
            return False
    return True

safe_levels = 0
for level in levels:
    if is_safe(level, less_than) or is_safe(level, grater_than):
        safe_levels += 1

print(f"part 1 -> {safe_levels}")

def generate_subsets(i, og_set, subset, aux):
    if (
        i >= len(og_set) and
        len(subset) >= 1 and
        abs(len(og_set) - len(subset)) <= 1 and
        (is_safe(subset, less_than) or is_safe(subset, grater_than))
    ):
        aux[0] = True
        return
    elif i>= len(og_set) or aux[0]:
        return
    subset.append(og_set[i])
    generate_subsets(i+1, og_set, subset, aux)
    subset.pop()
    generate_subsets(i+1, og_set, subset, aux)

safe_levels = 0
for level in levels:
    is_current_safe = [False]
    generate_subsets(0, level, [], is_current_safe)
    if is_current_safe[0]:
        safe_levels += 1

print(f"part 2 -> {safe_levels}")