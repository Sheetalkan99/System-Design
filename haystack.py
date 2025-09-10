def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):  # stop early to avoid overflow
        if haystack[i:i+m] == needle:
            return i  # found at index i
    return -1  # not found

# Test cases:
print(strStr("hello", "ll"))   # Expected output: 2
print(strStr("abcdef", "cd"))  # Expected output: 2
print(strStr("sheetal", "tea"))# Expected output: -1
print(strStr("aaaaa", "bba"))  # Expected output: -1
print(strStr("abcabc", "abc")) # Expected output: 0
