from collections import Counter

list1 = []
list2 = []

with open('./day01.txt', 'r') as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = 0
for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])

print(f"part 1 -> {total_distance}")

reps = Counter(list2)
similarity_score = 0
for num in list1:
    if num in reps:
        similarity_score += num * reps[num]

print(f"part 2 -> {similarity_score}")