def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    character_dict = {}
    for word in text:
        character = word.split()
        for char in character:
            key = char.lower()
            character_dict[key] = character_dict.get(key,0) + 1
    return character_dict

def sort_on(dict):
    return dict["num"]
def sort_count_characters(count_dict):
    char_list = []
    for key,value in count_dict.items():
        new_dict = {"char": key,"num": value}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list 
