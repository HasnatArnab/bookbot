from stats import get_num_words

def main():
    contents=get_book_text('books/frankenstein.txt')
    print(get_num_words(contents))
    
def get_book_text(path_file):
    '''this function takes the filepath as argument and returns the content of that file'''
    with open(path_file) as f:
        file_content=f.read()
        return file_content



    

if __name__ == "__main__":
    main()