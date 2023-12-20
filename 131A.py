def change(word: str):
    all = word.upper()
    butFirst = word[0].lower() + all[1:]
    if word == all:
        return word.lower()
    if word == butFirst:
        return word.capitalize()
    return word

print(change(input()))