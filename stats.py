def count_words(text):
    words = text.split()
    return len(words)

def count_each_character(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    sorted = []
    for char in char_count:
        sorted.append({'char': char, 'count': char_count[char]})

    def sort_on(item):
        return item['count']

    sorted.sort(key=sort_on, reverse=True)
    return sorted
