def uniq_char(s):
    if len(s) == 1:
        return True

    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True

test_str_true = 'fghij'
test_str_false = 'fgghij'

print(test_str_true)
print(uniq_char(test_str_true))
print (test_str_false)
print(uniq_char(test_str_false))
