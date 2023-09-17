def main():
    file = "books/frankenstein.txt"
    file_content = open_file(file)
    words_number = count_words(file_content)
    letts = letters(file_content)
    list = [(k, v) for k, v in letts.items()]
    list.sort(key= lambda x: x[1], reverse= True)
    report(words_number, list)
#
#
def open_file(file):
    with open(file) as f:
        content = f.read()
    return content.split()
#
#
def count_words(file_content):
    print(f"there is {len(file_content)} words")
    return len(file_content)
#
#
def letters(file_content):
    letters = {}
    for i in range(0, len(file_content)):
        for y in range(0, len(file_content[i])):
            if (
                is_alphabetic(file_content[i][y]) and
                file_content[i][y].lower() in letters
            ):
                letters[file_content[i][y].lower()] +=1
            elif (
                is_alphabetic(file_content[i][y])  and 
                file_content[i][y].lower() not in letters
            ):
                letters[file_content[i][y].lower()] = 1
    return letters
#
#
def is_alphabetic(character):
    return (character.lower() >= 'a' and character.lower() <= 'z')
#
#
def report(words_number, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_number} was found in the document")
    print("")
    for element in list:
        print(f" The '{element[0]}' character was found {element[1]} times")
    print("--- End report ---")
#
#
main()