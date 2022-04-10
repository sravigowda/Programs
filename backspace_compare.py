def backspace_compare(str1, str2):
    if string_remove(str1) == string_remove(str2):
        return True
    return False


def string_remove(test_str):
    index = 0
    substr = []
    while index < len(test_str):
        if test_str[index] != "#":
            substr.append(test_str[index])
        else:
            substr.pop()
        index += 1

    substr = "".join(substr)
    return substr

  
def backspace_compare_new(str1, str2):
    index_1 = len(str1) - 1
    index_2 = len(str2) - 1
    while index_1 > 0 and index_2 > 0:
        i1 = get_next_valid_character(str1, index_1)
        i2 = get_next_valid_character(str2, index_2 )
        if i1 < 0 and i2 < 0:
            return True
        elif i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False

        index_1 = i1 - 1
        index_2 = i2 - 1

    return True


def get_next_valid_character(str,index):
    backspace_count = 0
    while index >= 0:
        if str[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1

    return index

 def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))
    
    print(backspace_compare_new("xy#z", "xzz#"))
    print(backspace_compare_new("xy#z", "xyz#"))
    print(backspace_compare_new("xp#", "xyz##"))
    print(backspace_compare_new("xywrrmp", "xywrrmu#p"))


main()
