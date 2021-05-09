import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide=input("Press y for yes or n for no : ")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            print("Not closer word")
    else:
        print("Wrong word")
a="y"
while a =="y":
    word=input("Enter the word to search : ")
    result=translate(word)
    if result==list:
        for item in result:
            print(item)
    else:
        print(result)
    a=input("Check another type y : ")
