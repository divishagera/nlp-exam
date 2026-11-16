# 2a: Write a Python program to create a list with n values. The list of
# integers with exactly two occurrences of nineteen and at least three
# occurrences of five. Return True Otherwise False.
# Sample inputs/outputs: [19, 19, 15, 5, 3, 5, 5, 2] -> True; [19, 15, 15, 5, 3,
# 3, 5, 2] -> False; [19, 19, 5, 5, 5, 5, 5] -> True.

def check_list_condition(nums):
  return nums.count(19) == 2 and nums.count(5) >= 3


if __name__ == "__main__":
  n = int(input("Enter the number of elements (n): "))
  nums = []

  for i in range(n):
    val = int(input(f"Enter integer at index {i}: "))
    nums.append(val)

  print("User list:", nums)
  print("Output:", check_list_condition(nums))
