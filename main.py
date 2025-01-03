from tkinter.filedialog import askopenfilename

def main():
    book_path = askopenfilename()
    try:
        file_contents = get_book_text(book_path)
        print(f"File scanned at: {book_path}")
    except:
        print(f"File opening error")

    word_count = count_words(file_contents)
    character_dict = clean_dictionary(get_word_dictionary(file_contents))


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_word_dictionary(text: str) -> dict:
    words_dict = {}
    for word in text:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


# This takes in the dictionary of single letters from the count characters function
def clean_dictionary(d: dict) -> dict:
    temp_dict, clean_dict = {"word":"","count":0}, {}
    list_of_dict = []
    i=0
    
    # Introduce new k,v pairs as "letter:abc" and "count:123" 
    # where abc is the actual letter, and 123 is the actual count
    for element in d:        
            temp_dict["word"] = element 
            temp_dict["count"] = d[element]
            list_of_dict.append(dict(letter=element,count=d[element])) # Append these 2 pair dictionaries to list
    
    # Sort on "count" pair
    list_of_dict.sort(reverse=True, key=sort_on)

    # Build a new dictionary only of letter:count pairs
    for i in range(len(list_of_dict)):
        clean_dict[list_of_dict[i]["word"]] = list_of_dict[i]["count"]

    return clean_dict


def sort_on(dictionary):
    return dictionary["count"]


if __name__ == "__main__":    
    main()
    
