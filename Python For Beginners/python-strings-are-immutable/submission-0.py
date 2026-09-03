def remove_fourth_character(word: str) -> str:
    truff=word[:3]
    le=word[4:]
    drink=truff + le
    return drink


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
