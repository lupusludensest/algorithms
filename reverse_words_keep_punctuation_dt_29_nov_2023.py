# Задачка: развернуть все слова в предложении. Например, "How are you today."
# должно превратиться в "woH era uoy yadot." По невнимательности можно не заметить
# точку в конце предложения. И довольно просто обработать, если там только точка,
# и только в конце — проверяешь её наличие, отрезаешь, ревёрсишь каждое слово,
# соединяешь с пробелами, и добавляешь сохранённую точку (или любой другой знак препинания).
# Сложности начинаются, если вдруг внутри предложения есть другие знаки препинания.
# Или если преложений — два подряд. Вот решение:

import re

def reverse_words_keep_punctuation(sentence):
    """
    Function takes a sentence with or without punctuation marks within it and at the end.
    It reverses each word but keeps the order of the words and all punctuations at their places.
    """
    # Regular expression pattern to match words
    pattern = r'\b\w+\b'

    # Function to reverse a word
    def reverse_word(match):
        # print(len(match.group(0)))
        return match.group(0)[::-1]

    # Replace each word in the sentence with its reverse
    return re.sub(pattern, reverse_word, sentence)

# Example usage
print(reverse_words_keep_punctuation("How are you today"))
print(reverse_words_keep_punctuation("How are you today. Hope you are well."))
print(reverse_words_keep_punctuation("Hello, world!"))
print(reverse_words_keep_punctuation("What's the time?"))
print(reverse_words_keep_punctuation("Coding is fun, isn't it?"))
print(reverse_words_keep_punctuation("Однажды в студёную зимнюю пору я из дому вышел. Был сильный мороз."))