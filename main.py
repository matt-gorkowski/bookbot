def main():
    path_to_book = "./books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    print_report(word_count,letter_count,path_to_book)
    #return file_contents

def sort_on(dict):
    return dict["count"]

def count_words(file):
    words = file.split()
    return len(words)

def count_letters(file):
    letter_dict = {}
    for f in file:
        if f.isalpha():
            f = f.lower()
            if (f not in letter_dict):
                letter_dict[f] = 1
            else:
                letter_dict[f] += 1
    return letter_dict

def dict_to_list(letter_count):
    list_of_letters = []
    for l in letter_count:
        list_of_letters.append({'letter': l, 'count': letter_count[l]})
    return list_of_letters


def print_report(word_count,letter_count,path_to_book):
    list_of_letters = dict_to_list(letter_count)
    list_of_letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document\n")
    for l in list_of_letters:
        print(f"The {l['letter']} character was found {l['count']} times")
    print("--- End report ---")
    


main()