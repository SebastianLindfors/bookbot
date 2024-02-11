def get_file_contents(file_path):
    with open(file_path) as text_file:
        return text_file.read()


def get_word_count(input_string):
    words = input_string.split()
    return len(words)

def letter_count(input_string):
    letter_count_dict = {}
    for word in input_string.split():
        for char in word:
            if char.lower() in letter_count_dict:
                letter_count_dict[char.lower()] += 1
            else: 
                letter_count_dict[char.lower()] = 1

    return letter_count_dict


def create_book_report(file_path):

    file_contents = get_file_contents(file_path)
    word_count = get_word_count(file_contents)
    letter_count_dict = letter_count(file_contents)


    report_string = f"""--- Begin report of {file_path} ---
{word_count} words were found in the document

"""
    sorting_dict = []
    for key, value in letter_count_dict.items():
        if key.isalpha():
            sorting_dict.append({"letter": key, "occurences": value})

    def sort_on(dict):
        return dict["occurences"]
    
    sorting_dict.sort(reverse=True, key=sort_on)
    
    for entry in sorting_dict:
        report_string += f"The {entry["letter"]} character was found {entry["occurences"]} times\n"

    report_string += "--- End report ---"

    return report_string
    


def main():
    file_path = "books/frankenstein.txt"

    print(create_book_report(file_path))


main()