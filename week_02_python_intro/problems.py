def reverse_string(s):
    return s[::-1]

def find_max(lst):
    if not lst:
        return None
    return max(lst)

def is_palindrome(word):
    return word == word[::-1]