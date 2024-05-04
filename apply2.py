import random

# given a 2D list and a minimum and maximum value
# return 
def randomize(num_rows, num_columns, minimum, maximum):
    lst = [[0]*num_cols for _ in range(num_rows)]
    for r in range(num_rows):
        for c in range(num_columns):
            lst[r][c] = random.randint(minimum, maximum)
    return lst

def find_total(lst):
    total = 0
    for row in lst:
        for item in row:
            total += item
    return total


def find_min(lst):
    ans = 10000
    ans_row = 0
    ans_col = 0
    for r in range(len(lst)):
        for c in range(len(lst[0])):
            if lst[r][c] < ans:
                ans = lst[r][c]
                ans_row = r
                ans_col = c
    return ans, r, c


    

num_rows = int(input("how many rows? "))
num_cols = int(input("how many columns? "))
minimum = int(input("minimum value? "))
maximum = int(input("maximum value? "))

nums = randomize(num_rows, num_cols, minimum, maximum)

print("\nhere's the list")
print(nums)


print("sum is", find_total(nums))
smallest, r, c = find_min(nums)
print("smallest item is", smallest, "found at row", r, "and column", c)

        



# ---- challenge! ----
# create this list using loops:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
nums = []
counter = 0
for r in range(3):
    this_row = []
    for c in range(4):
       counter += 1
       this_row.append(counter)
    nums.append(this_row)
print("\na list created with loops")
print(nums) 