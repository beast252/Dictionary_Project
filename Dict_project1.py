import json
from difflib import get_close_matches
data = json.load(open(r"practice\Dictionary\data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        a= input("do you mean this word %s ? if yes type Y, else N "%(get_close_matches(w,data.keys())[0]))
        if a=='Y'or a=='y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return ["The word doesn't exist. Please Check it"]
    else:
        return["The word doesn't exist. Please Check it"]
word=input('Enter the Word: ')
print('\n'.join(translate(word)))
