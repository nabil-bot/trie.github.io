from nextWordPrediction import add_word

import pickle


with open("banglaWords.pkl", 'rb') as f:
    banglaWords = pickle.load(f)

print(type(banglaWords))
with open("words_set.pkl", "rb") as f:
    word_set = pickle.load(f)

print(f"\nBefore:\nNum of words from words_set.pkl file: {len(word_set)}\nNum of words in banglaWords.pkl: {len(banglaWords)}")

for word in word_set:
    # add_word(word)
    banglaWords.add(word)


with open("banglaWords.pkl", 'wb') as f:
    pickle.dump(banglaWords, f)

print(f"\nAfter:\nNum of words in banglaWords.pkl: {len(banglaWords)}")
