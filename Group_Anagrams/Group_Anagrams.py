from collections import defaultdict

def group_anagrams(a):
    anagram = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        anagram[sorted_i].append(i)
    return anagram.values()


words = ["race", "arc", "care", "heart", "earth", "ate", "car", "tea"]
print(group_anagrams(words))
