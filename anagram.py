import sys
def check_anagram(s1:str, s2:str):
    if len(s1) != len(s2):
        return 'not anagram'
    dicts1 = {}
    dicts2 = {}
    for char in s1:
        if dicts1.get(char):
            dicts1[char] = dicts1[char] + 1
        else:
            dicts1[char] = 1
    for char in s2:
        if dicts2.get(char):
            dicts2[char] = dicts2[char] + 1
        else:
            dicts2[char] = 1
    
    for key,value in dicts1.items():
        if dicts2[key] != value:
            return 'Not anagram'
    return 'Two string is anagram'


if __name__ == "__main__":
    s1 = input("enter s1:")
    s2 = input("enter s2:")
    print(check_anagram(s1,s2))