# here is the TLDR for 2D lists
# most common actions: create, access, loop

# create a list of zeros
nums = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]


# create a list of zeros, easier way
# 5 rows and 4 columns
nums = [[0]*4 for _ in range(5)]
print("\ncheck it out")
print(nums)


print("\naccess one item")
nums[2][3] = 'X'
print(nums)


print("\nenhanced loops:")
for row in nums:
    for item in row:
        print(item, end=" ")
    print()
    
    
print("\nindexed loops")
for r in range(len(nums)):
    for c in range(len(nums[0])):
        print(nums[r][c], end=" ")
    print()