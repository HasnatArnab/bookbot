import sys
from stats import get_num_words,get_num_char,sorted_list,generate_report

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath=sys.argv[1]
        contents=get_book_text(filepath)
        word_count=get_num_words(contents)
        char_list=get_num_char(contents)
        list=sorted_list(char_list)
        generate_report(filepath,word_count,list)
        
def get_book_text(path_file):
    '''this function takes the filepath as argument and returns the content of that file'''
    with open(path_file) as f:
        file_content=f.read()
        return file_content


if __name__ == "__main__":
    main()