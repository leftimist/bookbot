from tkinter.filedialog import askopenfilename
import pandas as pd
import os
import matplotlib.pyplot as plt


def main():
    book_path = askopenfilename() # Point to file
    try:
        file_contents = get_book_text(book_path)
        print(f"File scanned at: {book_path}")
    except:
        print(f"File opening error")

    # word_count = get_word_count(file_contents)
    word_dict = clean_dictionary(get_word_dictionary(file_contents))

    df = pd.DataFrame.from_dict(word_dict,"index",columns=["Count"])

    # Probably extract to different chart functions
    plt.figure()
    df.iloc[:10].plot(kind="barh",title="frankenstein")
    plt.show()


    save_output(book_path, word_dict)

    # Save output as csv with pandas
def save_output(input_fpath: str, input_dict: dict):
    current_path = os.getcwd()
    file_name = os.path.splitext(os.path.basename(input_fpath))[0] # Filename w/o extension
    output_file_name = current_path + "/output/" + file_name + "_" + str(int(os.path.getatime(input_fpath))) + ".csv"
    df = pd.DataFrame.from_dict(input_dict,"index",columns=["Count"])
    df.to_csv(output_file_name)
    print(f"File saved as: {output_file_name}")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_word_dictionary(text: str) -> dict:
    words_dict, new_string = {}, ""
    for word in text.split():

        for letter in word: # Only lowercase letters, no symbols and signs
            if ord(letter) >= 97 and ord(letter) <= 122:
                new_string += letter

        if new_string not in words_dict:
            words_dict[new_string] = 1
        else:
            words_dict[new_string] += 1

        new_string = ""
        
    if "" in words_dict:
        del words_dict[""]

    return words_dict


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


# This takes in the dictionary of words from the count characters function
def clean_dictionary(input_dir: dict) -> dict:
    temp_dict, clean_dict = {"word":"","count":0}, {}
    list_of_dict = []
    i=0
    
    # Introduce new k,v pairs as "letter:abc" and "count:123" 
    # where abc is the actual letter, and 123 is the actual count
    for element in input_dir:        
            temp_dict["word"] = element 
            temp_dict["count"] = input_dir[element]
            list_of_dict.append(dict(word=element,count=input_dir[element])) # Append these 2 pair dictionaries to list
    
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
    
