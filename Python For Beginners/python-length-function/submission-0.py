def get_longer_word(word1: str, word2: str) -> str:
    
    if len(word1)>=len(word2):
        word=word1
    else:
        word=word2

    return word




# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
