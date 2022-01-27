
def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
    left = s[:half + add]
    right = s[half + add:]
    return right + left

string_test_odd = 'aaadefffg'
string_test_even = 'bbcchhii'

print(string_test_odd)
print(split_in_half(string_test_odd))
print(string_test_even)
print(split_in_half(string_test_even))

