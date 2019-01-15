import load_dictionary
word_list = load_dictionary.load('dictionaries/words.txt')
anagram_list = []

#input a SINGLE word or SINGLE name below to find its anagrams(s):
name = input('Enter a word or name: ')
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out list of anagrams
print()
if len(anagram_list) == 0:
    print("No anagrams found")
else:
    print("Anagrams =", *anagram_list, sep='\n')
