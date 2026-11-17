# 2a: Write a Python program to create a list with n values. The list of
# integers with exactly two occurrences of nineteen and at least three
# occurrences of five. Return True Otherwise False.
# Sample: Input: [19, 19, 15, 5, 3, 5, 5, 2] Output: True
# Input: [19, 15, 15, 5, 3, 3, 5, 2] Output: False
# Input: [19, 19, 5, 5, 5, 5, 5] Output: True

nums = []
n = int(input("enter the size (list): "))

for i in range(0, n):
    print("enter number at index ", i)
    item = int(input())
    nums.append(item)

print("user list is nums", nums)

def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3

print("original list")
print(nums)

result = test(nums)
print("test result:", result)
