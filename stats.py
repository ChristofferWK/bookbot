def word_count(string):
    words = string.split()
    return len(words)
def character_count(string):
    dict_of_chars = {}
    lowercase_string = string.lower()
    string_list = list(lowercase_string)
    for letter in string_list:
        if (letter in dict_of_chars) == False:
            dict_of_chars[letter] = 1
        else:
            dict_of_chars[letter] += 1
    return dict_of_chars
def sort_dictionary(dictionary):
    list_of_dicts = []
    for entry in dictionary:
        loop_dict = {}
        dict_with_char = next((d for d in list_of_dicts if d["char"] == entry), None)
        if dict_with_char == None:
            new_dict = {"char": entry, "num": dictionary[entry]}
            list_of_dicts.append(new_dict)
    return list_of_dicts
def helper_function(dictionary):
    return dictionary["num"]
def sort_list_of_dicts(dict_list):
    dict_list.sort(key=helper_function, reverse=True)
    return dict_list




        


    
