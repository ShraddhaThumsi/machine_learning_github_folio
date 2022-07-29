
def is_firstchar_lower(s):
    return s[0].islower()

def sort_a_string(s):
    words_of_string = s.split(' ')
    all_to_lower_array = [s.lower() for s in words_of_string]
    sorted_all_to_lower = sorted(all_to_lower_array)
    string_parts_to_return = []
    for item in sorted_all_to_lower:
        if item in words_of_string:
            string_parts_to_return.append(item)
        else:
            string_parts_to_return.append(item.capitalize())

    return ' '.join(string_parts_to_return)
#string = 'a sling Slung off her neck'
#string = 'apple ORANGE banana'
string = 'a cat that was big'
print('original string: ')
print(string)
print('sorted string: ')
print(sort_a_string(string))