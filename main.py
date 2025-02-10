def main():
    print("--- Being report of books/frankenstein.txt ---")

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        totalWords = len(words)
        print(f"{totalWords} words found in the document")

        file_contents = file_contents.lower()
        charCount = {}
        for char in file_contents:
            if(char.isalpha()):
                charCount[char] = charCount.get(char,0) + 1
        listOfCharCount = []
        for char, value in charCount.items():
            listOfCharCount.append({'char': char, 'value': value})
        listOfCharCount.sort(reverse=True, key=sort_on)
        for character in listOfCharCount:
            print(f"The '{character["char"]}' character was found {character["value"]} times")
        
        print("--- End report ---")

def sort_on(dict):
    return dict["value"]

main()