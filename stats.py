def get_num_words(content):
    text=content.split()
    num_words = len(text)
    # print(text)
    return f"Found {num_words} total words"