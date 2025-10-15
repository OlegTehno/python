def get_num_words(text):
    return len(text.split())

def get_character_frequency(text):
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq

def sort_on(item):
    return item["num"]

def sort_dictionary_by_value(dictionary):
    items = [{"char": k, "num": v} for k, v in dictionary.items()]
    items.sort(key=sort_on, reverse=True)
    return items