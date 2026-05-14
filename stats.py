def get_word_count(book):
    return len(book.split())

def get_char_count(book):
    result = {}
    for word in book:
        for char in word:
            if char.lower() in result:
                result[char.lower()] += 1
            else:
                result[char.lower()] = 1
    return result

def sort_on(items):
    return items["num"]

def get_sorted_dictionary(char_dict):
    result = []
    for char in char_dict:
        entry = {}
        entry["char"] = char
        entry["num"] = char_dict[char]
        result.append(entry)

    result.sort(reverse=True, key=sort_on)
    return result
