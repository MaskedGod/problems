def translate(text):
    vowels = "aeiou"
    pig_latin_words = []

    def translate_word(word):
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"

        if "qu" in word:
            qu_index = word.index("qu")
            return word[qu_index + 2 :] + word[: qu_index + 2] + "ay"

        for i, char in enumerate(word):
            if char in vowels or (char == "y" and i > 0):
                return word[i:] + word[:i] + "ay"

        return word + "ay"

    for word in text.split():
        pig_latin_words.append(translate_word(word))

    return " ".join(pig_latin_words)


print(translate("yellow"), "ellowyay")
print(translate("quick fast run"), "ickquay astfay unray")
print("Rule 1------")
print(translate("apple"), "appleay")  # "appleay"
print(translate("yttria"), "yttriaay")  #  "yttriaay"
print(translate("igloo"), "iglooay")  #  "iglooay"
print("Rule 2------")
print(translate("pig"))  #  "igpay"
print(translate("chair"))  #  "airchay"
print(translate("thrush"))  #  "ushthray"
print("Rule 3------")
print(translate("quick"))  #  "ickquay"
print(translate("square"))  #  "aresquay"
print("Rule 4---------")
print(translate("my"))  #  "ymay"
print(translate("rhythm"))  #  "ythmrhay"

#  TODO Regex
