import random


def randomize(num_items, minimum, maximum):
    lst = [0 for _ in range(num_items)]
    for i in range(len(lst)):
        lst[i] = random.randint(minimum, maximum)
    return lst


def find_total(lst):
    total = 0
    for item in lst:
        total += item
    return total


def find_minimum(lst):
    ans = lst[0]
    ans_index = 0
    for i in range(len(lst)):
        if lst[i] < ans:
            ans = lst[i]
            ans_index = i
    return ans, ans_index


# sample, list with 13 values, between 0 and 100
nums = randomize(13, 0, 100)
print("\nchecking list")
print(nums)

print("total is", find_total(nums))
smallest, smallest_place = find_minimum(nums)
print("min is", smallest, "found at", smallest_place)