# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!", "")

words = ["Hi! Hello!", "", "Oh, no!!!"]

for w in words:
    print("foo(\"%s\") -> \"%s\"" % (w, remove_exclamation_marks(w)))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    return s.replace("!", "", 1) if s.endswith("!") else s

words = ["Hi!", "Hi!!!", "!Hi"]

for w in words:
    print("remove(\"%s\") == \"%s\"" % (w, remove_last_em(w)))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    return ''.join(word for word in s.split() if "!" not in word or word.count("!") > 1)

words = ["Hi!", "Hi! Hi!", "Hi! Hi! Hi!", "Hi Hi! Hi!", "Hi! !Hi Hi!", "Hi! Hi!! Hi!", "Hi! !Hi! Hi!"]

for w in words:
    print("remove(\"%s\") === \"%s\"" % (w, remove_word_with_one_em(w)))