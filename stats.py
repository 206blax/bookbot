
def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count


def char_count(text):
    lc_txt = text.lower()
    char = {}
    for i in lc_txt:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char

def sort_on(num):
    return num["num"]

def sort_list(characters):
    my_list = []
    for char in characters:
        my_list.append({"char": char, "num": characters[char]})
    my_list.sort(reverse=True, key=sort_on)
    return my_list
