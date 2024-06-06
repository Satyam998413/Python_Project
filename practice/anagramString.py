from collections import Counter

def isAnagram(str1,str2):
    return Counter(str1)==Counter(str2)

print(isAnagram("developer","redevelop"))
print(isAnagram("Turing","Turning"))