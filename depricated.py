def count_characters(text: str) -> dict:
    character_dict = {}
    # in text.lower() forces the loop to be over each character and lowered
    for letter in text.lower():         
            if letter not in character_dict:
                character_dict[letter] = 1
            else:
                character_dict[letter] += 1           
    return character_dict

# This takes in the dictionary of single letters from the count characters function
def clean_dictionary(d: dict) -> dict:
    temp_dict, clean_dict = {"letter":"","count":0}, {}
    list_of_dict = []
    i=0
    
    # Introduce new k,v pairs as "letter:abc" and "count:123" 
    # where abc is the actual letter, and 123 is the actual count
    for element in d:        
        if ord(element) >= 97 and ord(element) <= 122: # purge non-lowercase letters
            temp_dict["letter"] = element 
            temp_dict["count"] = d[element]
            list_of_dict.append(dict(letter=element,count=d[element])) # Append these 2 pair dictionaries to list
    
    # Sort on "count" pair
    list_of_dict.sort(reverse=True, key=sort_on)

    # Build a new dictionary only of letter:count pairs
    for i in range(len(list_of_dict)):
        clean_dict[list_of_dict[i]["letter"]] = list_of_dict[i]["count"]

    return clean_dict

# build_book_report(book_path, word_count, character_dict)
def build_book_report(book_path: str, word_count: int, letter_dict: dict):
    report_string_start = f"--- Begin report of {book_path} ---\n{word_count} words found in the document"
    report_string_middle = "\n"

    for c in letter_dict:
        report_string_middle = report_string_middle + f"The '{c}' character was found {letter_dict[c]} times\n"

    report_string_end = "--- End report ---"
    print(report_string_start + report_string_middle + report_string_end)

    