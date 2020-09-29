'''
def function(a):
    return a.title()
print(function("abca dsd"))
'''


def my_function(a):
    individual_word = a.split(' ')
    absolute = []
    for i in individual_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        absolute.append(word)
    return absolute


print(my_function("hello world"))
