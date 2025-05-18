def contains_duplicate(nums):
    # Use a set to track seen numbers
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def two_sum(nums, target):
    # Use a dictionary to store seen numbers and their indices
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def is_anagram(s, t):
    # Use sorted to compare characters. also convert to lowercase to make it case-insensitive
    return sorted(s.lower()) == sorted(t.lower())