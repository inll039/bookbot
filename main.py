def main():
    file = "books/frankenstein.txt"
    file_content = open_file(file)
    words_number = count_words(file_content)
    letts = letters(file_content)
#
#
def open_file(file):
    with open(file) as f:
        content = f.read()
    file_content = content.split()
    return file_content
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
    print(letters)
    return letters
#
#
def is_alphabetic(character):
    return (character.lower() >= 'a' and character.lower() <= 'z')
#
#
main()