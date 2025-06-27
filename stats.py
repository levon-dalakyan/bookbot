def count_words(string):
    return len(string.split())

def chars_amounts(string):
    lowered_string = string.lower()
    chars_dict = {}
    for s in lowered_string:
        if s in chars_dict:
            chars_dict[s] += 1
        else:
            chars_dict[s] = 1
    return chars_dict

def sort_on(item):
    return item["num"]

def dict_to_sorted_dicts(chars_dict):
    list = []
    for i in chars_dict:
        list.append({"char": i, "num": chars_dict[i]})
    list.sort(key=sort_on, reverse=True)
    return list
