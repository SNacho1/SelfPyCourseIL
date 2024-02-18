def sort_anagrams(list_of_strings):
    anagrams = []
    anagram_dict = {}
    
    for word in list_of_strings:
        anagram = ''.join(sorted(word))
        if anagram not in anagram_dict:
            anagram_dict[anagram] = [word]
        else:
            anagram_dict[anagram].append(word)
    
    for anagram in anagram_dict.values():
        anagrams.append(anagram)
    anagrams.sort(key=len, reverse=True)
    return anagrams
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
