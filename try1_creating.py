# ---- different ways to create a 2D list ----
print("\ncreate a 2D list using assignment")
nums1 = [
    [1,2,3],
    [4,5]
]
print(nums1)


print("\ncreate a 2D list using *")
print("this is a very common way, basically initialize to zeros")
nums2 = [[0]*5 for _ in range(7)]
print(nums2)

# note: nums = [0*c]*r does not work
# this creates copies of the row memory address, not copies of contents

print("\ncreate a 2D list using .append()")
print("this shows that a 2D list is actually a 'list of lists'")
one = ['a', 'b', 'c']
two = [42, 13, True]
nums4 = []
nums4.append(one)
nums4.append(two)
print(nums4)
