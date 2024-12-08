s = "is2 Thi1s T4est 3a"

def order(sentence):
    words = {}
    for word in sentence.split():
        for char in word:
            if char.isdigit():
                words[int(char)] = word

    sort_words = {key: words[key] for key in sorted(words)}
    return ' '.join(sort_words.values())

def order2(sentence):
  return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))

print(order(s))