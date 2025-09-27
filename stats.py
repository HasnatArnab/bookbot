def get_num_words(content):
    text=content.split()
    num_words = len(text)
    # print(text)
    return num_words

def get_num_char(content):
    char_list={}
    for i in content:
        i=i.lower()
        if not(i in char_list):
            char_list[i]=1
        else:
            char_list[i]+=1
    return char_list

def sorted_list(char_list):
    updated_list=[]
    for i in char_list:
        if i.isalpha():
            updated_list.append({"char":i, "num":char_list[i]})
    updated_list.sort(reverse=True,key=sort_on)
    return updated_list

def sort_on(items):
    return items["num"]

def generate_report(filepath,word_count,list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for i in list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")